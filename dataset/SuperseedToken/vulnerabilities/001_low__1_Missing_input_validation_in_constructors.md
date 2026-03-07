# .1 Missing input validation in constructors

**Severity:** low
**Auditor:** Cantina
**Protocol:** SuperseedToken
**Keywords:** input validation, constructors, TokenClaim, SuperseedToken, address validation, require statements, smart contracts, solidity, security, best practices, error handling, constructor parameters, IERC20, Ownable, ERC20, ERC20Permit, roles, minting, treasury, superAdmin

---

# .1 Missing input validation in constructors
**Severity:** Low Risk  
**Context:** TokenClaim.sol, SuperseedToken.sol  
**Description:** Both contracts in scope (TokenClaim and SuperseedToken) lack input validation on their constructors.  
**Recommendation:** Validate the following parameters:
- **TokenClaim:**
    \u0060\u0060\u0060solidity
    constructor(address _initialOwner, address _token, address _treasury) Ownable(_initialOwner) {
        require(_token != address(0), "invalid address");
        require(_treasury != address(0), "invalid address");
        token = IERC20(_token);
        treasury = _treasury;
    }
    \u0060\u0060\u0060
- **SuperseedToken:**
    \u0060\u0060\u0060solidity
    constructor(
        address superAdmin,
        address minter,
        address treasury
    )
        ERC20("Superseed", "SUPR")
        ERC20Permit("Superseed")
    {
        require(treasury != address(0), "invalid address");
        require(superAdmin != address(0), "invalid address");
        require(minter != address(0), "invalid address");
        _mint(treasury, 10_000_000_000e18);
        _grantRole(DEFAULT_ADMIN_ROLE, superAdmin);
        _grantRole(MINTER_ROLE, minter);
    }
    \u0060\u0060\u0060
**Superseed:** Fixed in commits 9cc97c94 and 69e15ade.  
**CantinaManaged:** Fix verified.
