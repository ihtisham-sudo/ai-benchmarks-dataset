# Audinarey - \u0060update_period(..)\u0060 leads to wrong calculation in weekly emissions breaking accounting for the protocol

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Velocitimeter V4
**Keywords:** cyber security, vulnerability, update_period, emissions calculation, team emissions, protocol accounting, weekly emissions, overestimation, minting, FLOW, circulating supply, Minter, manual review, inflated values, third party protocols, VELOCIMETER, reward distribution, gauge, discrepancy, impact

---

Audinarey

Medium

# \u0060update_period(..)\u0060 leads to wrong calculation in weekly emissions breaking accounting for the protocol

## Summary

The \u0060update_period(..)\u0060 function does the calculation and distribution of voter weekly and  \u0060_teamEmissions\u0060 of FLOW. However, the \u0060_teamEmissions\u0060 calculations is over estimated making the calculation wrong and more

## Vulnerability Detail

The \u0060_teamEmissions\u0060 is calculated on top of normal weekly emissions in the \u0060update_period()\u0060 function on L119

\u0060\u0060\u0060solidity
File: Minter.sol
112:     function update_period() external returns (uint) { // @audit 
113:         uint _period = active_period;
114:         if (block.timestamp >= _period + WEEK && initializer == address(0)) { // only trigger if new week
115:             _period = (block.timestamp / WEEK) * WEEK;
116:             active_period = _period;
117:             uint256 weekly = weekly_emission(); // could be just 2k if voter has notified reward
118:             
119:  ->         uint _teamEmissions = (teamRate * weekly) /
120:  ->             (PRECISION - teamRate);
121:             uint _required =  weekly + _teamEmissions;
122:             uint _balanceOf = _flow.balanceOf(address(this));
123:             if (_balanceOf < _required) {
124:  ->             _flow.mint(address(this), _required - _balanceOf);
\u0060\u0060\u0060

Ideally , the evaluation should work as follows 

- \u0060weeklyPerGauge\u0060 = 2000e18, \u0060teamRate\u0060 = 5% and \u0060numberOfGauges\u0060 = 0
- it is expected that 100e18 be minted and transferred to the \u0060teamEmissions\u0060 address and 2000e18 be  transferred to the \u0060Voter\u0060 as rewards
- bringing the total distributed (both team and voter) to 2100e18 for that epoch.

However as shown below, the \u0060teamEmissions\u0060 calculation breaks this accounting

\u0060\u0060\u0060solidity
// uint _teamEmissions = = (teamRate * weekly) / (PRECISION - teamRate);
_teamEmissions = (50 * 2000e18) / (1000 - 50)
_teamEmissions = 105e18
\u0060\u0060\u0060

Notice Now that 

- the evaluation of \u0060_teamEmissions\u0060 is 105e18 bringing the total to 2105e18 emmited for that epoch
- also the actual value now recieved by  is \u0060_teamEmissions\u0060 is 5.25% of the \u0060weekly\u0060 emmisions instead of 5%

This descrepancy becomes larger as the \u0060numberOfGauges\u0060 increases.

This can also lead to inflated values of \u0060Minter.circulating_supply()\u0060 because the total supply of flow is increased contrary to the expected rate owing to each mint action (L124) that may occur due to excess \u0060_teamEmissions\u0060 of FLOW calculated when \u0060update_period\u0060 is called. This could break accounting also for protocol who integrate with VELOCIMETER and use the \u0060circulating_supply()\u0060 function for core accounting

\u0060\u0060\u0060solidity
File: Minter.sol
93:     function circulating_supply() public view returns (uint)
94:         return _flow.totalSupply() - _ve.totalSupply();
95:     }

\u0060\u0060\u0060

## Impact

More FLOW is minted to team due to wrong calculation breaking accounting for the protocol and possible third party protocols who integrate with the protocol

## Code Snippet
https://github.com/sherlock-audit/2024-06-velocimeter/blob/main/v4-contracts/contracts/Minter.sol#L112-L120

## Tool used

Manual Review

## Recommendation

Modify the \u0060Minter::update_period()\u0060 function as shown below

\u0060\u0060\u0060diff
File: Minter.sol
112:     function update_period() external returns (uint) { // @audit
113:         uint _period = active_period;
114:         if (block.timestamp >= _period + WEEK && initializer == address(0)) { // only trigger if new week
115:             _period = (block.timestamp / WEEK) * WEEK;
116:             active_period = _period;
117:             uint256 weekly = weekly_emission(); // could be just 2k if voter has notified reward
118:
-119:             uint _teamEmissions = (teamRate * weekly) /
-120:               (PRECISION - teamRate);
+119:             uint _teamEmissions = (teamRate * weekly) /
+120:               (PRECISION);
121:             uint _required =  weekly + _teamEmissions;
122:             uint _balanceOf = _flow.balanceOf(address(this));
123:             if (_balanceOf < _required) {
124:                 _flow.mint(address(this), _required - _balanceOf);

\u0060\u0060\u0060
