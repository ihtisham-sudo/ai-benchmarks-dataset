# Lack of a two-step process for admin role transfers

**Severity:** HIGH
**Auditor:** TrailOfBits

---

## Security Assessment Report

## Difficulty: High

## Type: Data Validation

## Target
- `pool_manager.py`
- `pool.py`
- `loan.py`
- `lp_token_oracle.py`
- `oracle_adapter.py`

## Description
The Folks Finance methods used to transfer the admin role from one address to another perform those transfers in a single step, immediately updating the admin address. Making such a critical change in a single step is error-prone and can lead to irrevocable mistakes. These methods include the `update_admin` method, which is used to update the address of the `pool_manager` application’s admin. If the `update_admin` method were called with an incorrect address, it would no longer be possible to execute administrative actions such as the addition of a pool.

**CODE REDACTED**

**Figure 2.1:** REDACTED

The `update_admin` methods of the `pool`, `loan`, `lp_token_oracle`, and `oracle_adapter` applications also perform admin role transfers in a single step.

## Exploit Scenario
Alice, the admin of the `pool_manager` application, calls the `update_admin` method with an incorrect address. As a result, she permanently loses access to the admin role, and new pools cannot be added to the `pool_manager` application.

## Recommendations
**Short term:** Implement a two-step process for admin role transfers. One way to do this would be splitting each `update_admin` method into two methods: a `propose_admin` method that saves the address of the proposed new admin to the global state and an `accept_admin` method that finalizes the transfer of the role (and must be called by the address of the new admin).

**Long term:** Identify and document all possible actions that can be taken by privileged accounts and their associated risks. This will facilitate reviews of the codebase and help prevent future mistakes.

---

**Trail of Bits**  
Folks Finance Security Assessment  
**PUBLIC**
