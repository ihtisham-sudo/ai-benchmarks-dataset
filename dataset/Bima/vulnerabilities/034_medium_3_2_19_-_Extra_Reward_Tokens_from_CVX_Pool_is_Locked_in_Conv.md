# 3.2.19 - Extra Reward Tokens from CVX Pool is Locked in Convex Deposit Token Forever

**Severity:** medium
**Auditor:** Cantina
**Protocol:** Bima 
**Keywords:** ConvexDepositToken, reward token, BaseRewardPool, crvRewards, cvxRewards, getReward, extra rewards, transfer, contract, stuck, fetchRewards, stake, mock, integration, tokens, withdraw, arbitrary, balances, function, vulnerability

---

# 3.2.18 Receiver Inactivity Check
\u0060\u0060\u0060solidity
vm.prank(users.owner);
bimaVault.setReceiverIsActive(RECEIVER_ID, false);
// Skip 2 weeks
vm.warp(block.timestamp + 5 weeks);
// User locks more tokens
// Updated the code to initially lock half of received tokens, now lock other half
_lockMoreTokens(INIT_BAB_TKN_TOTAL_SUPPLY / 2 / 2);
// User registers weights again
vm.prank(users.user1);
incentiveVoting.registerAccountWeight(users.user1, 10);
// warp time by input
vm.warp(block.timestamp + 1 weeks * 10);
// cache state prior to allocateNewEmissions
uint16 finalWeek = SafeCast.toUint16(bimaVault.getWeek());
for (uint16 week = startWeek; week <= finalWeek; week++) {
   uint256 receiverWeight = incentiveVoting.getReceiverWeightAt(RECEIVER_ID, week);
   console.log("Weight at Week %s: %s", week, receiverWeight);
}
\u0060\u0060\u0060
Check that the receiver is active in all functions used for assigning voting power to receivers.

## 3.2.19 Extra Reward Tokens from CVX Pool is Locked in Convex Deposit Token Forever
Submitted by AngryMustacheMan  
Severity: Medium Risk  
Context: (No context files were provided by the reviewer)  
Summary: ConvexDepositToken fetches reward token from BaseRewardPool. For crvRewards, it correctly disables the extra reward tokens but for cvxRewards it uses the generic getReward() function without disabling extra rewards, hence receiving those rewards onto ConvexDepositToken.sol, but the ConvexDepositToken.sol doesn\u0027t have a function to transfer out these tokens, hence they get stuck in the contract forever.

BaseRewardPool of Convex finance allows using mainly 2 different methods to get rewards:
1. \u0060function getReward(address _account, bool _claimExtras) public\u0060
2. \u0060function getReward() external returns(bool)\u0060

As can be seen at #L980 - #L998 in the mainnet address 0x3Fe65692bfCD0e6CF84cB1E7d24108E434A7587e. The second one sets extra rewards to true by default. As it can be seen, the crv Reward pool sets extra rewards to false but cvxReward pool uses the second method here:
\u0060\u0060\u0060solidity
// ConvexDepositToken.sol#L284C1-L285C32:
crvRewards.getReward(address(this), false);
cvxRewards.getReward(); //<@here
\u0060\u0060\u0060
So the extra rewards are received by ConvexDepositToken.sol contract here. But the problem is it doesn\u0027t have a function to transfer out these extra rewards from the contract, similar to the one present in Curve Proxy as can be seen here:
\u0060\u0060\u0060solidity
// CurveProxy.sol#L255C3-L268C6:
\u0060\u0060\u0060
## Transfer Arbitrary Token Balances Out of This Contract

\u0060\u0060\u0060solidity
/**
 @notice Transfer arbitrary token balances out of this contract
 @dev Necessary for handling extra rewards on older gauge types
 */
function transferTokens(
  address receiver,
  TokenBalance[] calldata balances
) external onlyDepositManager returns (bool success) {
  for (uint256 i; i < balances.length; i++) {
     balances[i].token.safeTransfer(receiver, balances[i].amount);
  }
  success = true;
}
\u0060\u0060\u0060

Extra tokens are withdrawn on behalf of ConvexDepositToken.sol, but there is no way to transfer them out causing them to be stuck on ConvexDepositToken.sol contract forever.

Happens every time ConvexDepositToken.sol#_fetchRewards is called.

As I couldn\u0027t find integration tests for ConvexFinance, I created mock integrations to replicate a similar situation. Create a Mock_test folder inside the test folder and copy paste these 6 files to replicate a similar situation:

1. MockBaseRewardPool.sol:
\u0060\u0060\u0060solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "./MockConvexDepositToken.sol";

contract MockBaseRewardPool {
  using SafeERC20 for ERC20;
  ERC20 stakingToken;
  ERC20 public rewardToken;
  ERC20 public extraRewardToken;
  address public operator;
  uint256 public pid;
  ConvexDepositToken convexDepositToken;
  mapping(address => uint256) public balances;
  mapping(address => uint256) public rewards;
  address[] public extraRewards;
  event RewardPaid(address indexed user, uint256 reward);

  constructor(
     address _stakingToken,
     address _rewardToken,
     address _extraRewardToken,
     address _operator,
     uint256 _pid,
     address _convexDepositToken
  ) {
     stakingToken = ERC20(_stakingToken);
     rewardToken = ERC20(_rewardToken);
     extraRewardToken = ERC20(_extraRewardToken);
     operator = _operator;
     pid = _pid;
     convexDepositToken = ConvexDepositToken(_convexDepositToken);
  }

  function stake(uint256 _amount) external {
     stakingToken.safeTransferFrom(msg.sender, address(this), _amount);
     balances[msg.sender] += _amount;
  }

  function earned(address _account) public view returns (uint256) {
     // Mock calculation of earned rewards
     return balances[_account] * 10 / 100; // 10% of the staked amount
  }
}
\u0060\u0060\u0060
## Function getReward Vulnerability

\u0060\u0060\u0060solidity
function getReward(address _account, bool _claimExtras) public returns (bool) {
    uint256 reward = earned(_account);
    if (reward > 0) {
        rewards[_account] = 0;
        rewardToken.safeTransfer(_account, reward);
        emit RewardPaid(_account, reward);
    }
    if (_claimExtras) {
        extraRewardToken.safeTransfer(_account, reward);
    }
    return true;
}
\u0060\u0060\u0060

\u0060\u0060\u0060solidity
function getReward() external returns (bool) {
    return getReward(msg.sender, true);
}
\u0060\u0060\u0060
## Function getBalance Vulnerability

\u0060\u0060\u0060solidity
function getBalance(address _account) public returns (uint256) {
    return balances[_account];
}
\u0060\u0060\u0060
## MockConvexDepositToken.sol

\u0060\u0060\u0060solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "./MockBaseRewardPool.sol";

interface IBaseRewardPool {
    function stake(uint256 _amount) external;
    function getReward(address _account, bool _claimExtras) external returns (bool);
    function getReward() external returns (bool);
}

contract ConvexDepositToken is ERC20 {
    IBaseRewardPool public crvRewards;
    IBaseRewardPool public cvxRewards;
    ERC20 stakingToken;

    constructor(address _crvRewards, address _cvxRewards, address _stakingToken)
        ERC20("Convex Deposit Token", "CVXDT")
    {
        crvRewards = IBaseRewardPool(_crvRewards);
        cvxRewards = IBaseRewardPool(_cvxRewards);
        stakingToken = ERC20(_stakingToken);
        stakingToken.approve(address(crvRewards), type(uint256).max);
        stakingToken.approve(address(cvxRewards), type(uint256).max);
    }

    function deposit(uint256 _amount) public {
        stakingToken.transferFrom(msg.sender, address(this), _amount);
        crvRewards.stake(50 ether);
        cvxRewards.stake(50 ether);
    }

    function fetchRewards() external {
        // Fetch rewards from CRV pool without claiming extra rewards
        crvRewards.getReward(address(this), false);
        // Fetch rewards from CVX pool, implicitly claims extra rewards
        cvxRewards.getReward();
    }
}
\u0060\u0060\u0060

\u0060\u0060\u0060solidity
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract MockExtraRewardToken is ERC20 {
    constructor() ERC20("Extra Reward Token", "XRT") {}

    function mint(address to, uint256 amount) external {
        _mint(to, amount);
    }

    function burn(address from, uint256 amount) external {
        _burn(from, amount);
    }
}
\u0060\u0060\u0060
## MockRewardToken.sol
\u0060\u0060\u0060solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract MockRewardToken is ERC20 {
    constructor() ERC20("Reward Token", "RTK") {}

    function mint(address to, uint256 amount) external {
        _mint(to, amount);
    }

    function burn(address from, uint256 amount) external {
        _burn(from, amount);
    }
}
\u0060\u0060\u0060
## MockStakingToken.sol
\u0060\u0060\u0060solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract MockStakingToken is ERC20 {
    constructor() ERC20("Staking Token", "STK") {}

    function mint(address to, uint256 amount) external {
        _mint(to, amount);
    }

    function burn(address from, uint256 amount) external {
        _burn(from, amount);
    }
}
\u0060\u0060\u0060
## MockTest.t.sol
\u0060\u0060\u0060solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
import "forge-std/Test.sol";
import "./MockConvexDepositToken.sol";
import "./MockBaseRewardPool.sol";
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "./MockRewardToken.sol";
import "./MockExtraRewardToken.sol";
import "./MockStakingToken.sol";
\u0060\u0060\u0060
## Contract Overview

\u0060\u0060\u0060solidity
contract ConvexDepositTokenTest is Test {
    MockBaseRewardPool crvRewardPool;
    MockBaseRewardPool cvxRewardPool;
    ConvexDepositToken convexDepositToken;
    MockStakingToken stakingToken;
    MockRewardToken rewardToken;
    MockExtraRewardToken extraRewardToken;
    address user = address(0x1);
    
    function setUp() public {
        stakingToken = new MockStakingToken();
        rewardToken = new MockRewardToken();
        extraRewardToken = new MockExtraRewardToken();
        // Deploy mock reward pools
        crvRewardPool = new MockBaseRewardPool(
            address(stakingToken),
            address(rewardToken),
            address(extraRewardToken),
            address(this),
            0,
            address(convexDepositToken)
        );
        cvxRewardPool = new MockBaseRewardPool(
            address(stakingToken),
            address(rewardToken),
            address(extraRewardToken),
            address(this),
            1,
            address(convexDepositToken)
        );
        // Deploy ConvexDepositToken
        convexDepositToken = new ConvexDepositToken(address(crvRewardPool), address(cvxRewardPool),
            address(stakingToken));
        // Mint and approve tokens for testing
        stakingToken.mint(user, 1000 ether);
        rewardToken.mint(address(crvRewardPool), 100 ether);
        extraRewardToken.mint(address(crvRewardPool), 100 ether);
        rewardToken.mint(address(cvxRewardPool), 100 ether);
        extraRewardToken.mint(address(cvxRewardPool), 100 ether);
        stakingToken.approve(address(crvRewardPool), type(uint256).max);
        stakingToken.approve(address(cvxRewardPool), type(uint256).max);
    }
    
    function testFetchRewards() public {
        // User stakes tokens into CRV reward pool
        vm.startPrank(user);
        stakingToken.approve(address(convexDepositToken), 100 ether);
        convexDepositToken.deposit(100 ether);
        vm.stopPrank();
        // Call fetchRewards on ConvexDepositToken
        convexDepositToken.fetchRewards();
        // Assert basic rewards are distributed to the ConvexDepositToken
        uint256 basicRewards = rewardToken.balanceOf(address(convexDepositToken));
        console.log("Basic reward token from both crv+ cvx pools", basicRewards);
        // assertEq(basicRewards, 10 ether, "Basic rewards should be distributed to ConvexDepositToken");
        // Assert extra rewards are NOT distributed due to \u0060false\u0060 in getReward
        uint256 extraRewards = extraRewardToken.balanceOf(address(convexDepositToken));
        console.log("Extra reward tokens from cvx pool ", extraRewards);
        // assertEq(extraRewards, 0, "Extra rewards should not be distributed");
    }
}
\u0060\u0060\u0060

## Test Command

Now use forge test --mt testFetchRewards -vvv to get the following output:
\u0060\u0060\u0060plaintext
62
\u0060\u0060\u0060
No files changed, compilation skipped  
Ran 1 test for test/Mock_test/MockTest.t.sol:ConvexDepositTokenTest  
[PASS] testFetchRewards() (gas: 258018)  
Logs:  
Basic reward token from both crv+ cvx pools 10000000000000000000  
Extra reward tokens from cvx pool 5000000000000000000 // <@here  
Suite result: ok. 1 passed; 0 failed; 0 skipped; finished in 11.83ms (3.56ms CPU time)  
Here we can see that the extra rewards are transferred to ConvexDepositToken.  
Recommendation: Either turn off the extra rewards functionality or create a function to withdraw those funds out similar to CurveProxy.
PAGE END
