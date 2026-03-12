# Issue L-1: Deficit is ignored as if it wasn\u0027t ever borrowed in IRM supply-demand logic, so interest rates will be shifted downward over time

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Aave V3
**Keywords:** deficit, IRM, interest rates, supply-demand logic, ReserveLogic, total debt, unbacked, liquidity, borrowUsageRatio, supplyUsageRatio, accruals, bad debt, liquidation, debt, aToken, interest rate strategy, reserve factor, virtual balance, liquidity rate, debt ceiling

---

# Issue L-1: Deficit is ignored as if it wasn\u0027t ever borrowed in IRM supply-demand logic, so interest rates will be shifted downward over time

Source: [GitHub Issue](https://github.com/sherlock-audit/2025-01-aave-v3-3-judging/issues/202)

deficit part of the borrowed funds are now ignored in IRM logic as total debt figure supplied there does not include deficit. This twists any supply-demand logic IRM have/will have as it shouldn\u0027t depend on the quality of the debt, but on the what was supplied to the pool and what was loaned from it only. Now deficit is treated as if it was never loaned, which is not correct. 

IRM interest rate logic is now twisted proportionally to the realized deficit value compared to the remaining active debt. This doesn\u0027t depend on the IRM logic itself as deficit is ignored on ReserveLogic call level.

deficit is not the same as unbacked in a way that there was no underlying supply for unbacked yet (first goes mint Unbacked, then back Unbacked), while there was supply for deficit (funds were supplied, loaned, then their accruals stopped when the debt was marked as bad, then there will be a coverage supply in eliminateReserveDeficit()). I.e. for interest rate logic were never supplied and were supplied, were lost and to be compensated are not the same situations.

Essentially this is a ReserveLogic issue, since any IRM logic has no chance to treat deficit correctly since it\u0027s not given to it as a parameter. Unlike supplyUsageRatio situation mixing Bridge initiated unbacked with deficit makes little sense for borrowUsageRatio, i.e. estimation of supply-demand situation of the pool, so it can\u0027t be calculated in any IRM logic.

In other words, totalDebt in IRM logic should include deficit, but can\u0027t as it\u0027s not provided by ReserveLogic\u0027s updateInterestRatesAndVirtualBalance():

ReserveLogic.sol
\u0060\u0060\u0060solidity
(uint256 nextLiquidityRate, uint256 nextVariableRate) =
  IReserveInterestRateStrategy(
    reserve.interestRateStrategyAddress
  ).calculateInterestRates(
      DataTypes.CalculateInterestRatesParams({
        unbacked: reserve.unbacked + reserve.deficit,
\u0060\u0060\u0060

DefaultReserveInterestRateStrategyV2.sol
\u0060\u0060\u0060solidity
// Code block continues...
\u0060\u0060\u0060
if (params.totalDebt != 0) {
    vars.availableLiquidity =
      params.virtualUnderlyingBalance +
      params.liquidityAdded -
      params.liquidityTaken;
    vars.availableLiquidityPlusDebt = vars.availableLiquidity + params.totalDebt;
    vars.borrowUsageRatio =
      params.totalDebt.rayDiv(vars.availableLiquidityPlusDebt);
    vars.supplyUsageRatio = params.totalDebt.rayDiv(
      vars.availableLiquidityPlusDebt + params.unbacked
    );
} else {
    Fortheprotocolaccountingviewpointdeficitisstillborrowedfromthereservesincethe
    borrowingwasdoneforit,whilerepayment(inanyform)wasn\u0027t. I.e. itisbeingborrowed
    similarly to the healthy debt, the difference is that deficit is expected to be repaid by
    Umbrella(writtenoff),whilehealthydebtisexpectedtoberepaidbytheborrower. Until
    therepaymentisdonebothtypesrepresentactivedebt,i.e. whatwaseverborrowed:
    totalDebt
    uint256
    >> The total borrowed from the reserve
    Thatis,withtheintroductionofthedeficittheinclusionofdeficittounbackeddoneas
    Certora#M-01mitigationdoesn\u0027tlooktobeenoughas,keepingthesamevariablesasin
    issue description, totDEBT is no longer the amount of money that was borrowed since
    deficit was borrowedandwasn\u0027tyetrepaid,soisstillborrowed,justbeingmarkedfora
    write off. I.e. for pool it\u0027s still a debt, but frozen and not yield bearing.
    It cannot be deemedasifitiswrittenoffalreadybecauseusageratiosandIRMlogicis
    basedonthebalancesoffunds,andthecorrespondingsupplysidebalanceispresent
    until aToken burn, i.e. supply reduction, on executeEliminateDeficit():
    LiquidationLogic.sol#L135-L158
    >>     IAToken(reserveCache.aTokenAddress).burn(
              msg.sender,
              reserveCache.aTokenAddress,
              balanceWriteOff,
              reserveCache.nextLiquidityIndex
            );
} else {
    // This is a special case to allow mintable assets (ex. GHO), which by
    // definition cannot be supplied
    // and thus do not use virtual underlying balances.
    // In that case, the procedure is 1) sending the underlying asset to the
    // aToken and
// 2) trigger the handleRepayment() for the aToken to dispose of those assets
IERC20(params.asset).safeTransferFrom(
  msg.sender,
  reserveCache.aTokenAddress,
  balanceWriteOff
);
// it is assumed that handleRepayment does not touch the variable debt balance
>>    IAToken(reserveCache.aTokenAddress).handleRepayment(
  msg.sender,
  // In the context of GHO it\u0027s only relevant that the address has no debt.
  // Passing the pool is fitting as it\u0027s handling the repayment on behalf of
  address(this),
  balanceWriteOff
);

GhoAToken.sol

/// @inheritdoc IAToken
function handleRepayment(
  address user,
  address onBehalfOf,
  uint256 amount
) external virtual override onlyPool {
  uint256 balanceFromInterest =
    _ghoVariableDebtToken.getBalanceFromInterest(onBehalfOf);
  if (amount <= balanceFromInterest) {
    _ghoVariableDebtToken.decreaseBalanceFromInterest(onBehalfOf, amount);
  } else {
    _ghoVariableDebtToken.decreaseBalanceFromInterest(onBehalfOf,
      balanceFromInterest);
    >>    IGhoToken(_underlyingAsset).burn(amount - balanceFromInterest);
  }
}

Internal Pre-conditions
Material deficit was formed for a debt reserve compared to the active debt.

External Pre-conditions
None, it\u0027s internal accounting.

Attack Path
The impact will be accrued automatically along with deficit formation.
## Impact

IRMlogic (any version of it) is artificially shifted towards low usage situation and lower interest rates, despite user funds might being fully/almost fully utilized.


As an example, let\u0027s suppose there is 900 USDC of deficit, 100 USDC of the healthy debt and 100 USDC of the available liquidity in the pool, unbacked. It will be:

- borrowUsageRatio = 100 / 200 = 0.500 in 3.3 and 1000 / 1100 = 0.909 in 3.2 (1)
- supplyUsageRatio = 100 / 1100 = 0.091 in 3.3 and 1000 / 1100 = 0.909 in 3.2 (2)

\u0060\u0060\u0060solidity
DefaultReserveInterestRateStrategyV2.sol
if (params.totalDebt != 0) {
  vars.availableLiquidity =
     params.virtualUnderlyingBalance +
     params.liquidityAdded -
     params.liquidityTaken;
  vars.availableLiquidityPlusDebt = vars.availableLiquidity + params.totalDebt;
  vars.borrowUsageRatio =
    params.totalDebt.rayDiv(vars.availableLiquidityPlusDebt);
  vars.supplyUsageRatio = params.totalDebt.rayDiv(
    vars.availableLiquidityPlusDebt + params.unbacked
  );
} else {
\u0060\u0060\u0060

supplyUsageRatio is a coefficient between yield generating debt, paying current Variable Borrow Rate, and yield requiring liquidity, receiving current Liquidity Rate:

\u0060\u0060\u0060solidity
DefaultReserveInterestRateStrategyV2.sol
vars.currentLiquidityRate = vars
  .currentVariableBorrowRate
  .rayMul(vars.supplyUsageRatio)
  .percentMul(PercentageMath.PERCENTAGE_FACTOR - params.reserveFactor);
\u0060\u0060\u0060

This way 3.3 version of (2), supplyUsageRatio = 100 / 1100 = 0.091, looks correct as it is 100 units generate yield, while 1100 units expecting it. 

On the other hand, borrowUsageRatio should push interest rate higher when the demand is high vs optimalUsageRatio and vice versa. So, 3.3 version of (1), borrowUsageRatio = 100 / 200 = 0.500 is not a correct representation of the supply-demand situation in the pool: liquidity supply is 1100, this is what was supplied and accrued so far, while the loan.
demandis1000,thisiswhatwastakenoutasdebtandaccruedasitsinterest,i.e. the3.2 version of (1), 1000 / 1100 = 0.909, is valid instead. In other words it is high demand, very low coverage situation: almost all the tokens suppliedareutilizedbyloans(1000of1100aretaken),whichhavelowcoverageforthe supply(100loansgenerateinterestfor1100supply,becauseofthebaddebt,represented bydeficit). By borrowUsageRatiocomputeditislowdemand,verylowcoverageinstead, whichdoesn\u0027trepresenttherealsituationandmisalignLPincentives. Thatis,thedeficit can\u0027tbeignoredforborrowdemandcalculationasdemand-supplyisafunctionofloan origination, which happensbeforedebtqualityisrealized. Whendebtisissuedthe demandisset,ifsupplyisfixedforthesakeoftheexample,andthedemanddoesn\u0027t changeifthatdebtturnedouttobebad,astheloanisoriginatedalreadyandthatis notreplayedwhenloanis§writtenoff. CurrentsituationcanbeequivalenttoshiftingoptimalUsageRatioandcanevensurpass that. RatedynamicsdependonexcessBorrowUsageRatio = (borrowUsageRatio - optimalUsageRatio) / (1 - optimalUsageRatio) = 1 - (1 - borrowUsageRatio) / (1 - optimalUsageRatio)whenborrowUsageRatio > optimalUsageRatio,andon borrowUsageRatio / optimalUsageRatiowhenborrowUsageRatio <= optimalUsageRatio. Continuingthesameexample(1),borrowUsageRatio = 100 / 200 = 0.500nowand1000 / 1100 = 0.909beforeignoringthedeficit,ifoptimalUsageRatio = 0.8it\u0027s borrowUsageRatio > optimalUsageRatioandexcessBorrowUsageRatio = (1 - 0.909) / (1 - 0.8) = 0.45. NooptimalUsageRatiocanmakeitequivalentwhenborrowUsageRatio == 0.5sinceevenwhenoptimalUsageRatio == 0it\u0027sexcessBorrowUsageRatio = (1 - 0.5) / (1 - 0) = 0.5 > 0.45.
## Mitigation

ConsiderincludingthedeficitintobothsidesoftheborrowUsageRatiofraction,e.g.:

\u0060\u0060\u0060solidity
if (params.totalDebt != 0) {
  vars.availableLiquidity =
    params.virtualUnderlyingBalance +
    params.liquidityAdded -
    params.liquidityTaken;
  vars.availableLiquidityPlusDebt = vars.availableLiquidity + params.totalDebt;
  -      vars.borrowUsageRatio =
  ֒→  params.totalDebt.rayDiv(vars.availableLiquidityPlusDebt);
  +      vars.borrowUsageRatio = (params.totalDebt +
  ֒→  params.deficit).rayDiv(vars.availableLiquidityPlusDebt + params.deficit);
  vars.supplyUsageRatio = params.totalDebt.rayDiv(
  -        vars.availableLiquidityPlusDebt + params.unbacked
  +        vars.availableLiquidityPlusDebt + params.unbacked + params.deficit
  );
}
\u0060\u0060\u0060
} else {
    return (0, vars.currentVariableBorrowRate);
}

As a side effect there will no longer be a jump in borrow Usage Ratio when deficit is increased on bad debt liquidations. Also new bad debt deficit will be treated similarly to the bad debt positions existing pre 3.3 release.

Since it requires adding a deficit variable there is no need to include it in unbacked:

ReserveLogic.sol
\u0060\u0060\u0060solidity
(uint256 nextLiquidityRate, uint256 nextVariableRate) =
    IReserveInterestRateStrategy(
        reserve.interestRateStrategyAddress
    ).calculateInterestRates(
        DataTypes.CalculateInterestRatesParams({
            unbacked: reserve.unbacked + reserve.deficit,
            deficit: reserve.deficit,
            liquidityAdded: liquidityAdded,
            liquidityTaken: liquidityTaken,
            totalDebt: totalVariableDebt,
            reserveFactor: reserveCache.reserveFactor,
            reserve: reserveAddress,
            usingVirtualBalance: reserveCache.reserveConfiguration.getIsVirtualAccActive(),
            virtualUnderlyingBalance: reserve.virtualUnderlyingBalance
        })
    );
\u0060\u0060\u0060

DataTypes.sol
\u0060\u0060\u0060solidity
struct CalculateInterestRatesParams {
    uint256 unbacked;
    uint256 deficit;
    uint256 liquidityAdded;
    uint256 liquidityTaken;
    uint256 totalDebt;
    uint256 reserveFactor;
    address reserve;
    bool usingVirtualBalance;
    uint256 virtualUnderlyingBalance;
}
\u0060\u0060\u0060

Protocol Team’s Response
The current approach models the possible withdrawals of the system.
It is assumed that the umbrella will always be able to cover the debt that the seized aTokens will not be withdrawn. Therefore, the modeling of the IR is sound. We’ll reconsider the suggested approach in a future upgrade.
## Issue L-2: Liquidator can avoid resolving bad debt with dust supply/transfer while seizing all the borrower\u0027s collateral

Source: [GitHub Issue](https://github.com/sherlock-audit/2025-01-aave-v3-3-judging/issues/203)

The protocol has acknowledged this issue.


Whenever a position with one collateral and many debt reserves is up for liquidation with claiming all the collateral, its debt reserves will be deemed bad debt and cleaned up during \u0060executeLiquidationCall()\u0060, which will bear a significant cost for a liquidator. To avoid that the liquidator can create an additional collateral for the borrower. For example, can send a dust amount of non-isolated mode aToken not used by them yet, enabling it as a collateral via \u0060executeFinalizeTransfer()\u0060. This can be used by liquidators routinely as profit enhancement and leaves all the bad debt intact with deficit not formed.


When \u0060vars.totalCollateralInBaseCurrency > vars.collateralToLiquidateInBaseCurrency\u0060 in \u0060executeLiquidationCall()\u0060, it is \u0060hasNoCollateralLeft == false\u0060 and bad debt clean-up is avoided. For a bad debt bearing position with many debt reserves, liquidators will do that as long as this is profitable, which can frequently be the case on L1.

## Internal Pre-conditions

Borrower being liquidated has one collateral, with other supplies being not used as collaterals, and a number of debts. This can be quite common since 3.3 spreading over many debt reserves comes as a natural remedy from 50% rule change from being debt reserve wise to the whole position wise.

## External Pre-conditions

Gas price is high on liquidations so paying for dust aToken transfer or supply on behalf is cheaper than covering gas costs of the deficit formation for all debt reserves of the borrower.
## Attack Path

The goal is to trigger \u0060setUsingAsCollateral(id, true)\u0060 with some additional action that doesn\u0027t require borrower participation. This can be supplied with \u0060onBehalfOf = borrower\u0060 on straightforward aToken transfer, which is cheaper:

\u0060\u0060\u0060solidity
executeFinalizeTransfer(), SupplyLogic.sol:
if (params.balanceToBefore == 0) {
    DataTypes.UserConfigurationMap storage toConfig = usersConfig[params.to];
    if (
        ValidationLogic.validateAutomaticUseAsCollateral(
            reservesData,
            reservesList,
            toConfig,
            reserve.configuration,
            reserve.aTokenAddress
        )
    ) {
        toConfig.setUsingAsCollateral(reserveId, true);
        emit ReserveUsedAsCollateralEnabled(params.asset, params.to);
    }
}
\u0060\u0060\u0060

## Impact

Since allowing the 50% of all the total debt to be liquidated at once is an extra payoff for liquidators at the expense of the borrowers in order to provide bad debt clearing and deficit formation, the failure to do so is a direct loss for the borrowers from the 3.3 release. I.e. in the described circumstances nothing changes bad debt vice, it\u0027s still unrealized and require manual DAO intervention (repaying on behalf), but borrowers now lose more LB to liquidators.


According to the contest snapshot, it\u0027s about 145k for aToken transfer with enabling the collateral. Supply looks to be more expensive, 176k.

\u0060\u0060\u0060json
AToken.transfer.json:
"full amount; receiver: ->enableCollateral": "144881",
\u0060\u0060\u0060

It\u0027s about 100k per an additional asset bad debt clean-up. Whenever a bad debt bearing borrower has more than 2 debt reserves with one of them capable to take all the collateral, it\u0027s profitable to transfer aToken and avoid the cleanup (100*k > 145 if k > 1, where k is number of additional debt reserves).
## Mitigation

Since user can always enable the collateral manually one way to control for the issue is to require that automatic use happens on non-dust amount addition only, e.g.:

\u0060\u0060\u0060solidity
function validateAutomaticUseAsCollateral(
  mapping(address => DataTypes.ReserveData) storage reservesData,
  mapping(uint256 => address) storage reservesList,
  DataTypes.UserConfigurationMap storage userConfig,
  DataTypes.ReserveConfigurationMap memory reserveConfig,
  uint256 amountInBaseCurrency,
  address aTokenAddress
) internal view returns (bool) {
  if (reserveConfig.getDebtCeiling() != 0) {
    // ensures only the ISOLATED_COLLATERAL_SUPPLIER_ROLE can enable collateral as
    // side-effect of an action
    IPoolAddressesProvider addressesProvider = IncentivizedERC20(aTokenAddress)
      .POOL()
      .ADDRESSES_PROVIDER();
    if (
      !IAccessControl(addressesProvider.getACLManager()).hasRole(
        ISOLATED_COLLATERAL_SUPPLIER_ROLE,
        msg.sender
      )
    ) return false;
  } else {
    // ensures that amount that triggered the action is not below minimum
    if (amountInBaseCurrency < LiquidationLogic.MIN_LEFTOVER_BASE) return false;
  }
  return validateUseAsCollateral(reservesData, reservesList, userConfig, reserveConfig);
}
\u0060\u0060\u0060

All the uses of \u0060validateAutomaticUseAsCollateral\u0060 will need to supply the base currency equivalent amount for the action, e.g.:

\u0060\u0060\u0060solidity
if (params.balanceToBefore == 0) {
  DataTypes.UserConfigurationMap storage toConfig = usersConfig[params.to];
  uint256 assetPrice = IPriceOracleGetter(params.oracle).getAssetPrice(params.asset);
  uint256 assetUnit = 10 ** reserve.configuration.getDecimals();
  uint256 amountInBaseCurrency = (params.amount * assetPrice) / assetUnit;
  if (
    ValidationLogic.validateAutomaticUseAsCollateral(
      reservesData,
\u0060\u0060\u0060
## Protocol Team’s Response

As stated on the docs, the system is designed as a “best effort” approach. Currently, due to the automation of collateral enabling, there are certain constraints that don’t allow a perfect solution in all scenarios. Dependent on gas price, chain bonus it might be possible to optimize liquidations by not resolving deficit.
PAGE END
