#!/usr/bin/env python3
"""
Collect smart contract audit datasets from SCAS and Solodit APIs.
Produces: code/ + vulnerabilities/ per protocol for AI benchmarking.
"""

import os
import re
import sys
import json
import time
import shutil
import argparse
import subprocess
import urllib.request
import urllib.parse
import urllib.error
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

SCAS_BASE = "https://api.scauditstudio.com"
SOLODIT_BASE = "https://solodit.cyfrin.io/api/v1/solodit"
SOLODIT_API_KEY = os.getenv("SOLODIT_API_KEY", "")
DATASET_DIR = Path("dataset")

# FROM=110 is Sherlock, FROM=111 is another common source
KNOWN_FROM_VALUES = [110, 111, 112, 113, 114, 115]
MAX_ISSUES_PER_AUDIT = 80


def scas_get(path, quiet=False, retries=3):
    url = f"{SCAS_BASE}{path}"
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url)
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = resp.read().decode("utf-8")
                if not data.strip():
                    return None
                return json.loads(data)
        except urllib.error.HTTPError as e:
            if not quiet:
                print(f"  [WARN] SCAS HTTP {e.code}: {path}")
            return None
        except urllib.error.URLError as e:
            if attempt < retries - 1:
                time.sleep(2 * (attempt + 1))
                continue
            if not quiet:
                print(f"  [WARN] SCAS error: {path} -> {e}")
            return None
        except json.JSONDecodeError as e:
            if not quiet:
                print(f"  [WARN] SCAS JSON error: {path} -> {e}")
            return None


def solodit_post(endpoint, payload):
    url = f"{SOLODIT_BASE}{endpoint}"
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, method="POST")
    req.add_header("Content-Type", "application/json")
    req.add_header("X-Cyfrin-API-Key", SOLODIT_API_KEY)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except (urllib.error.HTTPError, urllib.error.URLError, json.JSONDecodeError) as e:
        print(f"  [WARN] Solodit error: {e}")
        return None


def fetch_all_protocols():
    print("[1/4] Fetching all published protocols from SCAS...")
    previews = scas_get("/report/preview/published/all")
    if not previews:
        print("  ERROR: Could not fetch protocol list")
        return []
    print(f"  Found {len(previews)} protocols")
    return previews


def fetch_protocol_details(name):
    encoded = urllib.parse.quote(name)
    return scas_get(f"/report/published/nouser/{encoded}")


def discover_from_value(rid):
    for from_val in KNOWN_FROM_VALUES:
        result = scas_get(f"/vulnerability/RID{rid}_AUDIT0_FROM{from_val}_ISSUE1", quiet=True)
        if result and isinstance(result, dict) and result.get("title"):
            return from_val
    return None


def fetch_scas_vulnerabilities(rid, from_val, report_amount):
    vulns = []
    consecutive_misses = 0

    for issue_num in range(1, MAX_ISSUES_PER_AUDIT + 1):
        vuln_id = f"RID{rid}_AUDIT0_FROM{from_val}_ISSUE{issue_num}"
        result = scas_get(f"/vulnerability/{vuln_id}", quiet=True)
        if result and isinstance(result, dict) and result.get("title"):
            vulns.append(result)
            consecutive_misses = 0
        else:
            consecutive_misses += 1
            if consecutive_misses >= 3:
                break

    return vulns


def fetch_solodit_findings(protocol_name):
    if not SOLODIT_API_KEY:
        return []

    all_findings = []
    page = 1

    while True:
        result = solodit_post("/findings", {
            "page": page,
            "pageSize": 100,
            "filters": {
                "keywords": protocol_name,
                "impact": ["HIGH"]
            }
        })
        if not result or "findings" not in result:
            break

        findings = result["findings"]
        all_findings.extend(findings)

        meta = result.get("metadata", {})
        if page >= meta.get("totalPages", 1):
            break
        page += 1
        time.sleep(3)

    return all_findings


def parse_github_url(url):
    """Extract base repo URL, branch, and subpath from GitHub URLs.
    e.g. https://github.com/org/repo/tree/main/src/core
      -> ('https://github.com/org/repo', 'main', 'src/core')
    """
    url = url.rstrip("/")
    match = re.match(r'(https://github\.com/[^/]+/[^/]+)(?:/tree/([^/]+)(?:/(.+))?)?', url)
    if match:
        return match.group(1), match.group(2), match.group(3)
    return url, None, None


def clone_github_repo(github_url, dest_dir, branch=None):
    if not github_url:
        return False

    github_url = github_url.rstrip("/")
    if not github_url.endswith(".git"):
        clone_url = github_url + ".git"
    else:
        clone_url = github_url

    cmd = ["git", "clone", "--depth", "1"]
    if branch:
        cmd += ["--branch", branch]
    cmd += [clone_url, str(dest_dir)]

    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=120
        )
        if result.returncode != 0:
            print(f"  [WARN] Git clone exit {result.returncode}: {result.stderr.strip()[:200]}")
            return False
        git_dir = dest_dir / ".git"
        if git_dir.exists():
            shutil.rmtree(git_dir)
        return dest_dir.exists()
    except Exception as e:
        print(f"  [WARN] Git clone failed: {e}")
        return False


def extract_solidity_files(repo_dir, code_dir, subpath=None):
    code_dir.mkdir(parents=True, exist_ok=True)
    count = 0
    skip_dirs = {"node_modules", "lib", "forge-std", ".git", "test", "tests", "script", "scripts"}

    search_root = repo_dir / subpath if subpath else repo_dir
    if not search_root.exists():
        search_root = repo_dir

    for sol_file in search_root.rglob("*.sol"):
        if not sol_file.is_file():
            continue
        parts = sol_file.relative_to(search_root).parts
        if any(p.lower() in skip_dirs for p in parts):
            continue
        if any(p.lower().startswith("mock") for p in parts):
            continue

        try:
            rel_path = sol_file.relative_to(search_root)
            dest = code_dir / rel_path
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(sol_file, dest)
            count += 1
        except Exception:
            continue

    return count


def save_vulnerability(vuln, vuln_dir, idx, source="scas"):
    vuln_dir.mkdir(parents=True, exist_ok=True)

    if source == "scas":
        severity = vuln.get("severity", "unknown")
        title = vuln.get("title", f"Issue {idx}")
        raw = vuln.get("raw", "")
        company = vuln.get("company", "")
        protocol = vuln.get("protocol", "")
        keywords = vuln.get("keywords", [])

        content = f"# {title}\n\n"
        content += f"**Severity:** {severity}\n"
        content += f"**Auditor:** {company}\n"
        content += f"**Protocol:** {protocol}\n"
        if keywords:
            content += f"**Keywords:** {', '.join(keywords)}\n"
        content += f"\n---\n\n{raw}\n"

        filename = f"{idx:03d}_{sanitize_filename(severity)}_{sanitize_filename(title[:60])}.md"
    else:
        severity = vuln.get("impact", "unknown")
        title = vuln.get("title", f"Issue {idx}")
        body = vuln.get("content", "")
        firm = vuln.get("firm_name", "")

        content = f"# {title}\n\n"
        content += f"**Severity:** {severity}\n"
        content += f"**Auditor:** {firm}\n"
        content += f"\n---\n\n{body}\n"

        filename = f"{idx:03d}_{sanitize_filename(severity)}_{sanitize_filename(title[:60])}.md"

    filepath = vuln_dir / filename
    filepath.write_text(content, encoding="utf-8")
    return severity


def sanitize_filename(name):
    return "".join(c if c.isalnum() or c in "-_ " else "_" for c in str(name)).strip().replace(" ", "_")


def main():
    parser = argparse.ArgumentParser(description="Collect audit vulnerability dataset")
    parser.add_argument("--dry-run", action="store_true", help="Only list protocols, don't download")
    parser.add_argument("--protocol", type=str, help="Process only a specific protocol by name")
    parser.add_argument("--skip-code", action="store_true", help="Skip GitHub code download")
    args = parser.parse_args()

    protocols = fetch_all_protocols()
    if not protocols:
        sys.exit(1)

    results = []

    for i, preview in enumerate(protocols):
        rid = preview.get("rid")
        name = preview.get("name", f"Unknown_{rid}")

        if args.protocol and args.protocol.lower() != name.lower():
            continue

        print(f"\n[{i+1}/{len(protocols)}] {name} (RID={rid})")

        details = fetch_protocol_details(name)
        if not details:
            print(f"  Skip: no details")
            continue

        github_url = details.get("codeBaseLink", "")
        total_reports = details.get("pastAudits", {}).get("reportAmount", 0)

        if not github_url:
            print(f"  Skip: no GitHub link")
            continue

        if total_reports < 1:
            print(f"  Skip: no audit reports")
            continue

        # Discover FROM value quickly
        from_val = discover_from_value(rid)

        high_vulns = []
        all_vulns = []
        vuln_source = "none"

        if from_val is not None:
            print(f"  FROM={from_val}, fetching vulns...")
            all_vulns = fetch_scas_vulnerabilities(rid, from_val, total_reports)
            high_vulns = [v for v in all_vulns if v.get("severity", "").lower() == "high"]
            vuln_source = "scas"
            print(f"  {len(all_vulns)} total, {len(high_vulns)} HIGH")

            # Check formatting quality
            if all_vulns:
                poorly_formatted = sum(1 for v in all_vulns if not v.get("raw", "").strip())
                if poorly_formatted > len(all_vulns) * 0.5:
                    print(f"  Poorly formatted ({poorly_formatted}/{len(all_vulns)})")
                    vuln_source = "needs_fallback"
        else:
            print(f"  No SCAS pattern found")
            vuln_source = "needs_fallback"

        # Solodit fallback
        if vuln_source == "needs_fallback" and SOLODIT_API_KEY:
            print(f"  Trying Solodit...")
            solodit_findings = fetch_solodit_findings(name)
            if solodit_findings:
                high_vulns = solodit_findings
                all_vulns = solodit_findings
                vuln_source = "solodit"
                print(f"  Solodit: {len(solodit_findings)} HIGH")

        if not high_vulns:
            print(f"  Skip: no HIGH vulns")
            continue

        print(f"  ✓ {len(high_vulns)} HIGH via {vuln_source}")

        if args.dry_run:
            results.append({
                "name": name, "rid": rid, "github": github_url,
                "total_vulns": len(all_vulns), "high_vulns": len(high_vulns),
                "source": vuln_source, "total_reports": total_reports
            })
            continue

        # Save vulnerabilities
        protocol_dir = DATASET_DIR / sanitize_filename(name)
        vuln_dir = protocol_dir / "vulnerabilities"

        severities = {"high": 0, "medium": 0, "low": 0, "other": 0}
        for idx, vuln in enumerate(all_vulns, 1):
            sev = save_vulnerability(vuln, vuln_dir, idx, source=vuln_source)
            sev_lower = sev.lower()
            if sev_lower in severities:
                severities[sev_lower] += 1
            else:
                severities["other"] += 1

        # Clone code
        sol_count = 0
        if not args.skip_code:
            repo_url, branch, subpath = parse_github_url(github_url)
            print(f"  Cloning {repo_url} (branch={branch}, subpath={subpath})...")
            tmp_repo = Path("/tmp") / f"repo_{rid}"
            if tmp_repo.exists():
                shutil.rmtree(tmp_repo)

            if clone_github_repo(repo_url, tmp_repo, branch=branch):
                code_dir = protocol_dir / "code"
                sol_count = extract_solidity_files(tmp_repo, code_dir, subpath=subpath)
                print(f"  {sol_count} Solidity files extracted")
                shutil.rmtree(tmp_repo, ignore_errors=True)
            else:
                print(f"  Clone failed, skipping code")

        # Save metadata
        metadata = {
            "name": name, "rid": rid,
            "score": details.get("score"),
            "category": details.get("category"),
            "github_url": github_url,
            "total_audit_reports": total_reports,
            "vulnerability_source": vuln_source,
            "vulnerability_counts": severities,
            "solidity_files": sol_count,
            "description": details.get("codeComplexity", {}).get("description", ""),
        }
        (protocol_dir / "metadata.json").write_text(
            json.dumps(metadata, indent=2), encoding="utf-8"
        )

        results.append({
            "name": name, "rid": rid, "github": github_url,
            "total_vulns": len(all_vulns), "high_vulns": len(high_vulns),
            "sol_files": sol_count, "source": vuln_source
        })

        print(f"  ✓ Saved to {protocol_dir}")

    # Summary
    print("\n" + "=" * 70)
    print("DATASET COLLECTION SUMMARY")
    print("=" * 70)
    print(f"{'Protocol':<30} {'High':>5} {'Total':>6} {'Source':<10}")
    print("-" * 70)
    for r in results:
        print(f"{r['name']:<30} {r['high_vulns']:>5} {r['total_vulns']:>6} {r['source']:<10}")
    print("-" * 70)
    print(f"Total protocols: {len(results)}")
    print(f"Total HIGH vulns: {sum(r['high_vulns'] for r in results)}")

    if not args.dry_run and results:
        save_dataset_index(results)


def save_dataset_index(results):
    index_path = DATASET_DIR / "README.md"
    lines = ["# AI Benchmark Audit Dataset\n"]
    lines.append(f"**Total protocols:** {len(results)}\n")
    lines.append(f"**Total HIGH vulnerabilities:** {sum(r['high_vulns'] for r in results)}\n\n")
    lines.append("| Protocol | HIGH | Total Vulns | Sol Files | Source | GitHub |")
    lines.append("|----------|------|-------------|-----------|--------|--------|")
    for r in results:
        gh = f"[link]({r['github']})" if r.get("github") else "-"
        lines.append(f"| {r['name']} | {r['high_vulns']} | {r['total_vulns']} | {r.get('sol_files', '-')} | {r['source']} | {gh} |")
    lines.append("")
    index_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nIndex saved to {index_path}")


if __name__ == "__main__":
    main()
