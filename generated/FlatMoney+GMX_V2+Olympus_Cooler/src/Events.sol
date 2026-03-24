// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * @title SyntheticVault — shared events and errors
 * @dev Synthesised from: FlatMoney, GMX_V2, Olympus_Cooler
 */
library SyntheticVaultEvents {

    // ── Events ─────────────────────────────────────────────────────
    event LeverageOpen(
        address account,
        uint256 tokenId,
        uint256 entryPrice,
        uint256 margin,
        uint256 size,
        uint256 tradeFee
    );
    event LeverageAdjust(
        uint256 tokenId,
        uint256 averagePrice,
        uint256 adjustPrice,
        int256 marginDelta,
        int256 sizeDelta,
        uint256 tradeFee
    );
    event LeverageClose(
        uint256 tokenId,
        uint256 closePrice,
        LeverageModuleStructs.PositionSummary positionSummary,
        uint256 settledMargin,
        uint256 size,
        uint256 tradeFee
    );
    event Deposit(address depositor, uint256 depositAmount, uint256 mintedAmount);
    event Withdraw(address withdrawer, uint256 withdrawAmount, uint256 burnedAmount, uint256 withdrawFee);
    event Locked(address indexed account, uint256 amount);
    event Unlocked(address indexed account, uint256 amount);
    event UnlockedAllLocks(uint256 tokenId, bytes32 indexed moduleKey);
    event LiquidationFeeRatioModified(uint256 oldRatio, uint256 newRatio);
    event LiquidationBufferRatioModified(uint256 oldRatio, uint256 newRatio);
    event LiquidationFeeBoundsModified(uint256 oldMin, uint256 oldMax, uint256 newMin, uint256 newMax);
    event PositionLiquidated(
        uint256 tokenId,
        address liquidator,
        uint256 liquidationFee,
        uint256 closePrice,
        LeverageModuleStructs.PositionSummary positionSummary
    );
    event SetMaxDiffPercent(uint256 maxDiffPercent);
    event SetOnChainOracle(OracleModuleStructs.OnchainOracle oracle);
    event SetOffChainOracle(OracleModuleStructs.OffchainOracle oracle);
    event OrderCancelled(address account, DelayedOrderStructs.OrderType orderType);
    event OrderExecuted(address account, DelayedOrderStructs.OrderType orderType, uint256 keeperFee);
    event LimitOrderExecuted(uint256 tokenId, LimitOrderExecutionType executionType);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);
    event ZapCompleted(address indexed sender, OrderType indexed orderType);
    event SwapComplete(address indexed router, SrcTokenSwapDetails indexed srcTokenSwapDetails);
    event RouterAdded(bytes32 indexed routerKey, address router);
    event RouterRemoved(bytes32 indexed routerKey);

    // ── Errors ─────────────────────────────────────────────────────
    error MaxPositionsInitZero();
    error MarginMismatchOnClose();
    error InsufficientGlobalMargin();
    error AddressNotWhitelisted(address account);
    error DepositCapReached(uint256 collateralCap);
    error InvalidLeverageCriteria();
    error MarginTooSmall(uint256 marginMin, uint256 margin);
    error LeverageTooLow(uint256 leverageMin, uint256 leverage);
    error LeverageTooHigh(uint256 leverageMax, uint256 leverage);
    error PriceImpactDuringWithdraw();
    error PriceImpactDuringFullWithdraw();
    error UnsupportedTokenTransferMethod();
    error NativeTokenSentWithoutNativeSwap();
    error InvalidNativeTokenTransferEncoding();
    error NotEnoughNativeTokenSent(uint256 expectedAmount, uint256 sentAmount);
    error UnsupportedPermit2Method(Permit2TransferType transferType);
    error AmountsAfterPermit2TransferMismatch(address token, uint256 expectedAmount, uint256 actualAmount);
    error ERC721OutOfBoundsIndex(address owner, uint256 index);
    error ERC721EnumerableForbiddenBatchMint();
    error CannotLiquidate(uint256 tokenId);

}