# 4.2 (HAL-02) REDUNDANT EVENTS ON THE RateLimitedMidpointLibrary - INFORMATIONAL (1.6)

**Severity:** info
**Auditor:** Halborn
**Protocol:** Moonwell
**Keywords:** redundant, events, RateLimitedMidpointLibrary, RateLimitPerSecondUpdate, BufferCapUpdate, RateLimitMidpointCommonLibrary, duplicate, event definitions, compiled contract, deployment costs, efficiency, contract size, optimization, removal, code quality, best practices, event emission, smart contract, solidity, Moonwell Finance

---

# 4.2 (HAL-02) REDUNDANT EVENTS ON THE RateLimitedMidpointLibrary - INFORMATIONAL (1.6)

### Description:
In the library, specifically within the RateLimitedMidpointLibrary, there are redundant event definitions for RateLimitPerSecondUpdate and BufferCapUpdate. These events are already defined in the RateLimitMidpointCommonLibrary. Additionally, having duplicate event definitions increases the size of the compiled contract unnecessarily, which can have implications on deployment costs and efficiency.

### Code Location:
RateLimitedMidpointLibrary.sol#L18C1-L25C7

### Listing 2
\u0060\u0060\u0060solidity
    /// @notice event emitted when buffer cap is updated
    event BufferCapUpdate(uint256 oldBufferCap, uint256 newBufferCap);

    /// @notice event emitted when rate limit per second is updated
    event RateLimitPerSecondUpdate(
        uint256 oldRateLimitPerSecond,
        uint256 newRateLimitPerSecond
    );
\u0060\u0060\u0060

### BVSS:
AO:A/AC:L/AX:L/C:N/I:M/A:N/D:N/Y:N/R:F/S:C (1.6)
## Recommendation:
Consider removing redundant events.
## Remediation Plan:
SOVLED: The Moonwell Finance team solved the issue by removing redundant events.
## Commit ID:
4e66e79485448ff31890a06618902135cace12d1
## DETAILS
## TECH
## FINDINGS
In the XERC20Lockbox, there is an import statement for SafeCast from OpenZeppelin’s contracts library, but upon reviewing the contract’s code, it appears that SafeCast is not being used. SafeCast is typically employed for safely casting between different numeric types, ensuring that the cast does not cause unintended overflows or underflows. However, in this contract, all operations involving uint256 types do not utilize any casting that would require SafeCast.

XERC20Lockbox.sol

\u0060\u0060\u0060solidity
contract XERC20Lockbox is IXERC20Lockbox {
    using SafeERC20 for IERC20;
    using SafeCast for uint256;
}
\u0060\u0060\u0060

BVSS:  
TECH AO:A/AC:L/AX:L/C:N/I:M/A:N/D:N/Y:N/R:F/S:C (1.6)
## Recommendation:
Since SafeCast is not utilized in the contract, it’s recommended to remove the import statement. This helps in reducing the contract’s compilation size and improves readability by eliminating unnecessary code.
SOLVED: The Moonwell Finance team solved the issue by removing the redundant SafeCast import.  
Commit ID: 45f7b230ab68e97c77e7f06abeb930dc6149d825
## FINDINGS
PAGE END
