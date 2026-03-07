# Issue 1 - Invalid Allocation Error in Managed Budget

**Severity:** high
**Auditor:** Sherlock
**Protocol:** Boost Protocol
**Keywords:** ManagedBudget, InitPayload, approve, ERC20, allocate, InvalidAllocation, feeOnTransfer, revert, sponsor, allocation, check, support, tokens, data, mockFeeOnTransferERC20, address, ether, AssetType, vm, error

---

                           abi.encode(                                 ManagedBudget.InitPayload({owner: address(this), authorized: new               ֒→  address[](0), roles: new uint256[](0)})                            )                        );                        mockFeeOnTransferERC20.approve(address(managedBudget), 100 ether);                        bytes memory data = _makeFungibleTransfer(ABudget.AssetType.ERC20,               ֒→  address(mockFeeOnTransferERC20), address(this), 100 ether);                        vm.expectRevert(abi.encodeWithSelector(ABudget.InvalidAllocation.selector,               ֒→  address(mockFeeOnTransferERC20), uint256(100 ether)));                        managedBudget.allocate(data);                   }             ThetestpasseswhichmeansthemanagedBudget.allocate(data)callrevertswithanInva             lidAllocationerror             Mitigation             This oneis tricky since there are 2 paths the sponsor can take:                 1. Removethesupportforfeeontransfertokensandmentionthisexplicitly                2. Keepsupportingfeeontransfertokensandremovetheaforementionedcheck.                                                               17 
