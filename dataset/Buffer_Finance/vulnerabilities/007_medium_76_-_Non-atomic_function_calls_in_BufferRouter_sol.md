# 76 - Non-atomic function calls in BufferRouter.sol

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Buffer Finance
**Keywords:** BufferRouter, non-atomic, ECDSA, signature validation, manual review, security, audit, Ethereum, smart contract, protocol, trading, function call, revert, error handling, transaction, signature, contract interaction, audit, security, Ethereum

---

# Vulnerability in BufferRouter.sol

**Code Snippet**  
[BufferRouter.sol](https://github.com/sherlock-audit/2022-11-buffer/blob/main/contracts/contracts/core/BufferRouter.sol#L350)

**Tool used**  
Manual Review

**Recommendation**  
Follow “Checks Effects Interactions”

\u0060\u0060\u0060solidity
function _openQueuedTrade(uint256 queueId, uint256 price) internal {
    ...
    +     queuedTrade.isQueued = false;
    // Transfer the fee to the target options contract
    IERC20 tokenX = IERC20(optionsContract.tokenX());
    tokenX.transfer(queuedTrade.targetContract, revisedFee);
    -     queuedTrade.isQueued = false;
    emit OpenTrade(queuedTrade.user, queueId, optionId);
}
\u0060\u0060\u0060

**Discussion**  
0x00052  
Fixed in PR#8  
Changes look good. Trade is now removed from queue before sending user refund during option opening to avoid potential reentrancy. Canceling already removed trade before sending refund so no change needed there.
**Source:** [GitHub Issue](https://github.com/sherlock-audit/2022-11-buffer-judging/issues/95)  
**Found by:** Ch_301  

_fee() function is wrongly implemented in the code so the protocol will get fewer fees and the trader will earn more.

\u0060\u0060\u0060solidity
(uint256 unitFee, , ) = _fees(10**decimals(), settlementFeePercentage);
amount = (newFee * 10**decimals()) / unitFee;
\u0060\u0060\u0060
Let\u0027s say we have: 
- newFee: 100 USDC 
- USDC Decimals: 6 
- settlementFeePercentage: 20% ==> 200

The unitFee will be 520_000.  
\u0060\u0060\u0060solidity
amount = (100 * 1_000_000) / 520_000 
amount = 192 USDC 
\u0060\u0060\u0060
Which is supposed to be  
\u0060\u0060\u0060solidity
amount = 160 USDC
\u0060\u0060\u0060

The protocol will earn fees less than expected.

\u0060\u0060\u0060solidity
function checkParams(OptionParams calldata optionParams)
    external
    view
    override
    returns (
        uint256 amount,
        uint256 revisedFee,
        bool isReferralValid
    )
{
    require(
        assetCategory != AssetCategory.Forex ||
\u0060\u0060\u0060
## \u0060\u0060\u0060solidity
isInCreationWindow(optionParams.period),
"O30"
);
uint256 maxAmount = getMaxUtilization();
// Calculate the max fee due to the max txn limit
uint256 maxPerTxnFee = ((pool.availableBalance() *
    config.optionFeePerTxnLimitPercent()) / 100e2);
uint256 newFee = min(optionParams.totalFee, maxPerTxnFee);
// Calculate the amount here from the new fees
uint256 settlementFeePercentage;
(
    settlementFeePercentage,
    isReferralValid
) = _getSettlementFeePercentage(
    referral.codeOwner(optionParams.referralCode),
    optionParams.user,
    _getbaseSettlementFeePercentage(optionParams.isAbove),
    optionParams.traderNFTId
);
(uint256 unitFee, , ) = _fees(10**decimals(), settlementFeePercentage);
amount = (newFee * 10**decimals()) / unitFee;
\u0060\u0060\u0060
[BufferBinaryOptions.sol](https://github.com/bufferfinance/Buffer-Protocol-v2/blob/83d85d9b18f1a4d09c72/8adaa0dde4c37406dfed/contracts/core/BufferBinaryOptions.sol#L318-L353)

\u0060\u0060\u0060solidity
function _fees(uint256 amount, uint256 settlementFeePercentage)
    internal
    pure
    returns (
        uint256 total,
        uint256 settlementFee,
        uint256 premium
    )
{
    // Probability for ATM options will always be 0.5 due to which we can skip
    ✱✦ using BSM
    premium = amount / 2;
    settlementFee = (amount * settlementFeePercentage) / 1e4;
    total = settlementFee + premium;
}
\u0060\u0060\u0060
[BufferBinaryOptions.sol](https://github.com/bufferfinance/Buffer-Protocol-v2/blob/83d85d9b18f1a4d09c72)
Manual Review

The \u0060fee()\u0060 function needs to calculate the fees in this way:
\u0060\u0060\u0060
total_fee = (5000 * amount) / (10000 - sf)
\u0060\u0060\u0060

0x00052  
Fixed in PR#22  
Changes look good. New math returns correct values. Validated for both unit fee and option amount.
**Source:** [GitHub Issue](https://github.com/sherlock-audit/2022-11-buffer-judging/issues/84)  
**Found by:** 0x52  

BufferRouter#resolveQueuedTrades and unlockOptions attempt to be non-atomic (i.e. doesn\u0027t revert the transaction if one fails) but an invalid signature can still cause the entire transaction to revert, because the ECDSA.recover sub call in _validateSigner can still revert.

\u0060\u0060\u0060solidity
function _validateSigner(
    uint256 timestamp,
    address asset,
    uint256 price,
    bytes memory signature
) internal view returns (bool) {
    bytes32 digest = ECDSA.toEthSignedMessageHash(
        keccak256(abi.encodePacked(timestamp, asset, price))
    );
    address recoveredSigner = ECDSA.recover(digest, signature);
    return recoveredSigner == publisher;
}
\u0060\u0060\u0060
_validateSigner can revert at the ECDSA.recover sub call breaking the intended non-atomic nature of BufferRouter#resolveQueuedTrades and unlockOptions.

BufferRouter#resolveQueuedTrades and unlockOptions don\u0027t function as intended if signature is malformed.

[BufferRouter.sol](https://github.com/sherlock-audit/2022-11-buffer/blob/main/contracts/contracts/core/BufferRouter.sol#L260-L271)
## Recommendation
Use a try statement inside \u0060_validateSigner\u0060 to avoid any reverts:
\u0060\u0060\u0060solidity
function _validateSigner(
   uint256 timestamp,
   address asset,
   uint256 price,
   bytes memory signature
) internal view returns (bool) {
   bytes32 digest = ECDSA.toEthSignedMessageHash(
      keccak256(abi.encodePacked(timestamp, asset, price))
   );
   try ECDSA.recover(digest, signature) returns (address recoveredSigner) {
      return recoveredSigner == publisher;
   } else {
      return false;
   }
}
\u0060\u0060\u0060
## Discussion
**bufferfinance**  
The protocol has been tested against wrong signatures. [Link to tests](https://github.com/sherlock-audit/2022-11-buffer/blob/main/contracts/tests/test_router.py#L815)  
0x00052  
Escalate for 10 USDC.  
My submission is valid and sponsor\u0027s comment here is inaccurate. ECDSA.recover will revert in the _throwError subcall under quite a few conditions not covered by their tests, including signature of invalid length and signature that resolve to address(0).  
[Link to ECDSA code](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/24d1bb668a1152528a6e6d71c2e285d227ed19d9/contracts/utils/cryptography/ECDSA.sol#L88-L92)  

**sherlock-admin**  
Escalate for 10 USDC.
Mysubmissionisvalid and sponsor\u0027s comment here is inaccurate.  
ECDSA.recover will revert in the _throwError subcall under quite a few conditions not covered by their tests, including signature of invalid length and signature that resolve to address(0).  
[Source Code](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/24d1bb668a1152528a6e6d71c2e285d227ed19d9/contracts/utils/cryptography/ECDSA.sol#L88-L92)  

You\u0027ve created a valid escalation for 10 USDC!  
To remove the escalation from consideration: Delete your comment. To change the amount you\u0027ve staked on this escalation: Edit your comment (do not create a new comment).  
You may delete or edit your escalation comment anytime before the 48-hour escalation window closes. After that, the escalation becomes final.  

hrishibhat  
Escalation accepted  
Invalid signatures resolving to address(0) reverts _validateSigner  

sherlock-admin  
Escalation accepted  
Invalid signatures resolving to address(0) reverts _validateSigner  

This issue\u0027s escalations have been accepted!  
Contestants\u0027 payouts and scores will be updated according to the changes made on this issue.  

bufferfinance  
Will fix this  

0x00052  
Fixed in PR#28  
Changes look good. ECDSA.recover changed to ECDSA.tryRecover to prevent any revert when recovering signatures
**Source:** [GitHub Issue](https://github.com/sherlock-audit/2022-11-buffer-judging/issues/76)  
**Found by:** supernova, rvierdiiev, eierina, cccz, KingNFT, dipp, __141345__, Bnke0x0, jonatascm, pashov, Deivitto  

The BufferBinaryPool.sol and BufferRouter.sol do not support fee-on-transfer tokens. If tokenX is a fee-on-transfer token, tokens received from users could be less than the amount specified in the transfer.

The \u0060initiateTrade\u0060 function in BufferRouter.sol receives tokens from the user with amounts set to \u0060initiateTrade\u0060\u0027s \u0060totalFee\u0060 input. If tokenX is a fee-on-transfer token then the actual amount received by BufferRouter.sol is less than \u0060totalFee\u0060. When a trade is opened, the protocol will send a \u0060settlementFee\u0060 to \u0060settlementFeeDisbursalContract\u0060 and a \u0060premium\u0060 to BufferBinaryPool.sol, where the \u0060settlementFee\u0060 is calculated using the incorrect, inflated \u0060totalFee\u0060 amount. When the \u0060totalFee\u0060 is greater than the fee required, the user is reimbursed the difference. Since the \u0060settlementFee\u0060 is greater than it should be, the user receives less reimbursement.

In BufferBinaryPool.sol\u0027s \u0060lock\u0060 function, the premium for the order is sent from the Options contract to the Pool. The \u0060totalPremium\u0060 state variable would be updated incorrectly if fee-on-transfer tokens were used.

The \u0060provide\u0060 function in BufferBinaryPool.sol receives \u0060tokenXAmount\u0060 of tokenX tokens from the user and calculates the amount of shares to mint using the \u0060tokenXAmount\u0060. If fee-on-transfer tokens are used then the user would receive more shares than they should.

The protocol and users could suffer a loss of funds.

\u0060\u0060\u0060solidity
BufferRouter.sol#L86-L90
BufferBinaryPool.sol#L161
\u0060\u0060\u0060
Manual Review

Consider checking the balance of the contract before and after token transfers and using instead of the amount specified in the contract.

0x00052  
Only an issue if project intends to support fee-on-transfer tokens as underlying bufferfinance.  
Notsupporting fee-on-transfer tokens for now.  
bufferfinance  
Buffer won\u0027t be supporting fee-on-transfer tokens. Thus we are not fixing it.
**Source:** [GitHub Issue #73](https://github.com/sherlock-audit/2022-11-buffer-judging/issues/73)  
**Found by:** m_Rassska, ctf_sec, ak1, cccz, Bnke0x0, 0x007, minhtrng, rvierdiiev, 0xadrii, hansfriese, 0xheynacho, HonorLt, bin2chen, eierina, aphak5010, __141345__, pashov, eyexploit, 0xcc, peanuts, sach1r0, 0x4non, adriro, jonatascm, Deivitto

Buffer contest states \u0027any ERC20 supported\u0027, therefore it should take into account all the different ways of signalling success and failure. This is not the case, as all ERC20\u0027s transfer(), transferFrom(), and approve() functions are either not verified at all or verified for returning true. As a result, depending on the ERC20 token, some transfer errors may result in passing unnoticed, and/or some successful transfer may be treated as failed.

Currently, the only supported ERC20 tokens are the ones that fulfill both the following requirements:
- always revert on failure;
- always returns boolean true on success.

An example of a very well-known token that is not supported is TetherUSD (USDT).

**IMPORTANT** This issue is not the same as reporting that "return value must be verified to be true" where the checks are missing! Indeed such a simplistic report should be considered invalid as it still does not solve all the problems but rather introduces others. See Vulnerability Details section for rationale.

Tokens have different ways of signalling success and failure, and this affects mostly transfer(), transferFrom() and approve() in ERC20 tokens. While some tokens revert upon failure, others consistently return boolean flags to indicate success or failure, and many others have mixed behaviours.

See below a snippet of the USDT Token contract compared to the 0x\u0027s ZRX Token contract where the USDT Token transfer function does not even return a boolean value, while the ZRX token consistently returns a boolean value hence returning false on failure instead of reverting.
## USDT Token snippet (no return value) from Etherscan
\u0060\u0060\u0060solidity
// Example code snippet
\u0060\u0060\u0060
## Code Snippet 1
\u0060\u0060\u0060solidity
function transferFrom(address _from, address _to, uint _value) public
    ✱✦ onlyPayloadSize(3 * 32) {
    var _allowance = allowed[_from][msg.sender];
    // Check is not needed because sub(_allowance, _value) will already throw if
    // this condition is not met
    // if (_value > _allowance) throw;
    uint fee = (_value.mul(basisPointsRate)).div(10000);
    if (fee > maximumFee) {
        fee = maximumFee;
    }
    if (_allowance < MAX_UINT) {
        allowed[_from][msg.sender] = _allowance.sub(_value);
    }
    uint sendAmount = _value.sub(fee);
    balances[_from] = balances[_from].sub(_value);
    balances[_to] = balances[_to].add(sendAmount);
    if (fee > 0) {
        balances[owner] = balances[owner].add(fee);
        Transfer(_from, owner, fee);
    }
    Transfer(_from, _to, sendAmount);
}
\u0060\u0060\u0060

## Code Snippet 2
\u0060\u0060\u0060solidity
function transferFrom(address _from, address _to, uint _value) returns (bool) {
    if (balances[_from] >= _value && allowed[_from][msg.sender] >= _value &&
        ✱✦ balances[_to] + _value >= balances[_to]) {
        balances[_to] += _value;
        balances[_from] -= _value;
        allowed[_from][msg.sender] -= _value;
        Transfer(_from, _to, _value);
        return true;
    } else { return false; }
}
\u0060\u0060\u0060

Given the different usages of token transfers in BufferBinaryOptions.sol,
BufferBinaryPool.sol, and BufferRouter.sol, there can be 2 types of impacts
depending on the ERC20 contract being traded.
The ERC20 token being traded is one that consistently returns a boolean result in the case of success and failure like for example 0x\u0027s ZRX Token contract. Where the return value is currently not verified to be true (i.e.: #1, #2, #3, #4, #5, #6) the transfer may fail (e.g.: no tokens transferred due to insufficient balance) but the error would not be detected by the Buffer contracts.

The ERC20 token being traded is one that does not return a boolean value like for example the well-known Tether USD Token contract. Successful transfers would cause a revert in the Buffer contracts where the return value is verified to be true (i.e.: #1, #2, #3, #4) due to the token not returning boolean results. Same is true for approve calls.

- [BufferRouter.sol#L86-L90](https://github.com/sherlock-audit/2022-11-buffer/blob/main/contracts/contracts/core/BufferRouter.sol#L86-L90)
- [BufferRouter.sol#L331](https://github.com/sherlock-audit/2022-11-buffer/blob/main/contracts/contracts/core/BufferRouter.sol#L331)
- [BufferRouter.sol#L335-L338](https://github.com/sherlock-audit/2022-11-buffer/blob/main/contracts/contracts/core/BufferRouter.sol#L335-L338)
- [BufferRouter.sol#L361-L364](https://github.com/sherlock-audit/2022-11-buffer/blob/main/contracts/contracts/core/BufferRouter.sol#L361-L364)
- [BufferBinaryOptions.sol#L141](https://github.com/sherlock-audit/2022-11-buffer/blob/main/contracts/contracts/core/BufferBinaryOptions.sol#L141)
- [BufferBinaryOptions.sol#L477](https://github.com/sherlock-audit/2022-11-buffer/blob/main/contracts/contracts/core/BufferBinaryOptions.sol#L477)
- [BufferBinaryPool.sol#L162](https://github.com/sherlock-audit/2022-11-buffer/blob/main/contracts/contracts/core/BufferBinaryPool.sol#L162)
- [BufferBinaryPool.sol#L205](https://github.com/sherlock-audit/2022-11-buffer/blob/main/contracts/contracts/core/BufferBinaryPool.sol#L205)
- [BufferBinaryPool.sol#L241](https://github.com/sherlock-audit/2022-11-buffer/blob/main/contracts/contracts/core/BufferBinaryPool.sol#L241)
- [BufferBinaryPool.sol#L323](https://github.com/sherlock-audit/2022-11-buffer/blob/main/contracts/contracts/core/BufferBinaryPool.sol#L323)

Manual Review

To handle most of these inconsistent behaviors across multiple tokens, either use OpenZeppelin\u0027s SafeERC20 library, or use a more reusable implementation (i.e. library) of the following intentionally explicit, descriptive example code for an ERC20 transferFrom() call that takes into account all the different ways of signaling.
## Vulnerability Details

The following code snippet demonstrates a vulnerability related to success and failure handling in ERC20 \u0060transfer()\u0060, \u0060transferFrom()\u0060, and \u0060approve()\u0060 calls in the Buffer contracts.

\u0060\u0060\u0060solidity
IERC20 token = whatever_token;
(bool success, bytes memory returndata) =
    address(token).call(abi.encodeWithSelector(IERC20.transferFrom.selector,
    sender, recipient, amount));
// if success == false, without any doubts there was an error and callee reverted
require(success, "Transfer failed!");
// if success == true, we need to check whether we got a return value or not
// (like in the case of USDT)
if (returndata.length > 0) {
    // we got a return value, it must be a boolean and it should be true
    require(abi.decode(returndata, (bool)), "Transfer failed!");
} else {
    // since we got no return value it can be one of two cases:
    // 1. the transferFrom does not return a boolean and it did succeed
    // 2. the token address is not a contract address therefore call() always
    // return success = true as per EVM design
    // To discriminate between 1 and 2, we need to check if the address actually
    // points to a contract
    require(address(token).code.length > 0, "Not a token address!");
}
\u0060\u0060\u0060

Fixed in PR#18. Changes look good. Using safeERC20 for ERC20 transfers.
PAGE END
