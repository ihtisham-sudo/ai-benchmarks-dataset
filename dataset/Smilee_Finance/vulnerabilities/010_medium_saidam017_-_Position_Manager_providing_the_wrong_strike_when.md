# saidam017 - Position Manager providing the wrong strike when storing user\u0027s position data

**Severity:** medium
**Auditor:** Sherlock
**Protocol:** Smilee Finance
**Keywords:** cybersecurity, vulnerability, PositionManager, strike data, mint position, user funds, contract, dvp.mint, current strike, premium calculation, position information, burn function, epoch, transaction execution, manual review, risk assessment, data storage, recommendation, smart contract, blockchain

---

saidam017

high

# Position Manager providing the wrong strike when storing user\u0027s position data

## Summary

When users mint position using \u0060PositionManager\u0060, users can provide strike that want to be used for the trade. However, if the provided strike data is not exactly the same with IG\u0027s current strike, the minted position\u0027s will be permanently stuck inside the \u0060PositionManager\u0060\u0027s contract.

## Vulnerability Detail

When \u0060mint\u0060 is called inside \u0060PositionManager\u0060, it will calculate the premium, transfer the required base token, and eventually call \u0060dvp.mint\u0060, providing the user\u0027s provided information.

https://github.com/sherlock-audit/2024-02-smilee-finance/blob/main/smilee-v2-contracts/src/periphery/PositionManager.sol#L129-L137

\u0060\u0060\u0060solidity
    function mint(
        IPositionManager.MintParams calldata params
    ) external override returns (uint256 tokenId, uint256 premium) {
        IDVP dvp = IDVP(params.dvpAddr);

        if (params.tokenId != 0) {
            tokenId = params.tokenId;
            ManagedPosition storage position = _positions[tokenId];

            if (ownerOf(tokenId) != msg.sender) {
                revert NotOwner();
            }
            // Check token compatibility:
            if (position.dvpAddr != params.dvpAddr || position.strike != params.strike) {
                revert InvalidTokenID();
            }
            Epoch memory epoch = dvp.getEpoch();
            if (position.expiry != epoch.current) {
                revert PositionExpired();
            }
        }
        if ((params.notionalUp > 0 && params.notionalDown > 0) && (params.notionalUp != params.notionalDown)) {
            // If amount is a smile, it must be balanced:
            revert AsymmetricAmount();
        }

        uint256 obtainedPremium;
        uint256 fee;
        (obtainedPremium, fee) = dvp.premium(params.strike, params.notionalUp, params.notionalDown);

        // Transfer premium:
        // NOTE: The PositionManager is just a middleman between the user and the DVP
        IERC20 baseToken = IERC20(dvp.baseToken());
        baseToken.safeTransferFrom(msg.sender, address(this), obtainedPremium);

        // Premium already include fee
        baseToken.safeApprove(params.dvpAddr, obtainedPremium);

==>     premium = dvp.mint(
            address(this),
            params.strike,
            params.notionalUp,
            params.notionalDown,
            params.expectedPremium,
            params.maxSlippage,
            params.nftAccessTokenId
        );

        // ....
    }
\u0060\u0060\u0060

Inside \u0060dvp.mint\u0060, in this case, IG contract\u0027s \u0060mint\u0060, will use \u0060financeParameters.currentStrike\u0060 instead of the user\u0027s provided strike: 
https://github.com/sherlock-audit/2024-02-smilee-finance/blob/main/smilee-v2-contracts/src/IG.sol#L75

\u0060\u0060\u0060solidity
    /// @inheritdoc IDVP
    function mint(
        address recipient,
        uint256 strike,
        uint256 amountUp,
        uint256 amountDown,
        uint256 expectedPremium,
        uint256 maxSlippage,
        uint256 nftAccessTokenId
    ) external override returns (uint256 premium_) {
        strike;
        _checkNFTAccess(nftAccessTokenId, recipient, amountUp + amountDown);
        Amount memory amount_ = Amount({up: amountUp, down: amountDown});

==>     premium_ = _mint(recipient, financeParameters.currentStrike, amount_, expectedPremium, maxSlippage);
    }
\u0060\u0060\u0060

But when storing the position\u0027s information inside \u0060PositionManager\u0060, it uses user\u0027s provided strike instead of IG\u0027s current strike : 
https://github.com/sherlock-audit/2024-02-smilee-finance/blob/main/smilee-v2-contracts/src/periphery/PositionManager.sol#L151-L160

\u0060\u0060\u0060solidity
    function mint(
        IPositionManager.MintParams calldata params
    ) external override returns (uint256 tokenId, uint256 premium) {
        // ...

        if (obtainedPremium > premium) {
            baseToken.safeTransferFrom(address(this), msg.sender, obtainedPremium - premium);
        }

        if (params.tokenId == 0) {
            // Mint token:
            tokenId = _nextId++;
            _mint(params.recipient, tokenId);

            Epoch memory epoch = dvp.getEpoch();

            // Save position:
            _positions[tokenId] = ManagedPosition({
                dvpAddr: params.dvpAddr,
==>             strike: params.strike,
                expiry: epoch.current,
                premium: premium,
                leverage: (params.notionalUp + params.notionalDown) / premium,
                notionalUp: params.notionalUp,
                notionalDown: params.notionalDown,
                cumulatedPayoff: 0
            });
        } else {
            ManagedPosition storage position = _positions[tokenId];
            // Increase position:
            position.premium += premium;
            position.notionalUp += params.notionalUp;
            position.notionalDown += params.notionalDown;
            /* NOTE:
                When, within the same epoch, a user wants to buy, sell partially
                and then buy again, the leverage computation can fail due to
                decreased notional; in order to avoid this issue, we have to
                also adjust (decrease) the premium in the burn flow.
             */
            position.leverage = (position.notionalUp + position.notionalDown) / position.premium;
        }

        emit BuyDVP(tokenId, _positions[tokenId].expiry, params.notionalUp + params.notionalDown);
        emit Buy(params.dvpAddr, _positions[tokenId].expiry, premium, params.recipient);
    }
\u0060\u0060\u0060

## PoC

Add the following test to \u0060PositionManagerTest\u0060 contract : 

\u0060\u0060\u0060solidity
    function testMintAndBurnFail() public {
        (uint256 tokenId, ) = initAndMint();
        bytes4 PositionNotFound = bytes4(keccak256("PositionNotFound()"));

        vm.prank(alice);
        vm.expectRevert(PositionNotFound);
        pm.sell(
            IPositionManager.SellParams({
                tokenId: tokenId,
                notionalUp: 10 ether,
                notionalDown: 0,
                expectedMarketValue: 0,
                maxSlippage: 0.1e18
            })
        );
    }
\u0060\u0060\u0060

Modify \u0060initAndMint\u0060 function to the following : 

\u0060\u0060\u0060solidity
    function initAndMint() private returns (uint256 tokenId, IG ig) {
        vm.startPrank(admin);
        ig = new IG(address(vault), address(ap));
        ig.grantRole(ig.ROLE_ADMIN(), admin);
        ig.grantRole(ig.ROLE_EPOCH_ROLLER(), admin);
        vault.grantRole(vault.ROLE_ADMIN(), admin);
        vault.setAllowedDVP(address(ig));

        MarketOracle mo = MarketOracle(ap.marketOracle());

        mo.setDelay(ig.baseToken(), ig.sideToken(), ig.getEpoch().frequency, 0, true);

        Utils.skipDay(true, vm);
        ig.rollEpoch();
        vm.stopPrank();

        uint256 strike = ig.currentStrike();

        (uint256 expectedMarketValue, ) = ig.premium(0, 10 ether, 0);
        TokenUtils.provideApprovedTokens(admin, baseToken, DEFAULT_SENDER, address(pm), expectedMarketValue, vm);
        // NOTE: somehow, the sender is something else without this prank...
        vm.prank(DEFAULT_SENDER);
        (tokenId, ) = pm.mint(
            IPositionManager.MintParams({
                dvpAddr: address(ig),
                notionalUp: 10 ether,
                notionalDown: 0,
                strike: strike + 1,
                recipient: alice,
                tokenId: 0,
                expectedPremium: expectedMarketValue,
                maxSlippage: 0.1e18,
                nftAccessTokenId: 0
            })
        );
        assertGe(1, tokenId);
        assertGe(1, pm.totalSupply());
    }
\u0060\u0060\u0060

Run the test : 

\u0060\u0060\u0060sh
forge test --match-contract PositionManagerTest --match-test testMintAndBurnFail -vvv
\u0060\u0060\u0060

## Impact

If the provided strike data does not match IG\u0027s current strike price, the user\u0027s minted position using \u0060PositionManager\u0060 will be stuck and cannot be burned. This happens because when burn is called and \u0060position.strike\u0060 is provided, it will revert as it cannot find the corresponding positions inside IG contract.

This issue directly risking user\u0027s funds, consider a scenario where users mint a position near the end of the rolling epoch, providing the old epoch\u0027s current price. However, when the user\u0027s transaction is executed, the epoch is rolled and new epoch\u0027s current price is used, causing the mentioned issue to occur, and users\u0027 positions and funds will be stuck.

## Code Snippet

https://github.com/sherlock-audit/2024-02-smilee-finance/blob/main/smilee-v2-contracts/src/periphery/PositionManager.sol#L129-L137
https://github.com/sherlock-audit/2024-02-smilee-finance/blob/main/smilee-v2-contracts/src/IG.sol#L75
https://github.com/sherlock-audit/2024-02-smilee-finance/blob/main/smilee-v2-contracts/src/periphery/PositionManager.sol#L151-L160

## Tool used

Manual Review

## Recommendation

When storing user position data inside PositionManager, query IG\u0027s current price and use it instead.


\u0060\u0060\u0060diff
    function mint(
        IPositionManager.MintParams calldata params
    ) external override returns (uint256 tokenId, uint256 premium) {
        // ...

        if (params.tokenId == 0) {
            // Mint token:
            tokenId = _nextId++;
            _mint(params.recipient, tokenId);

            Epoch memory epoch = dvp.getEpoch();
+          uint256 currentStrike = dvp.currentStrike();

            // Save position:
            _positions[tokenId] = ManagedPosition({
                dvpAddr: params.dvpAddr,
-                strike: params.strike,
+                strike: currentStrike,
                expiry: epoch.current,
                premium: premium,
                leverage: (params.notionalUp + params.notionalDown) / premium,
                notionalUp: params.notionalUp,
                notionalDown: params.notionalDown,
                cumulatedPayoff: 0
            });
        } else {
            ManagedPosition storage position = _positions[tokenId];
            // Increase position:
            position.premium += premium;
            position.notionalUp += params.notionalUp;
            position.notionalDown += params.notionalDown;
            /* NOTE:
                When, within the same epoch, a user wants to buy, sell partially
                and then buy again, the leverage computation can fail due to
                decreased notional; in order to avoid this issue, we have to
                also adjust (decrease) the premium in the burn flow.
             */
            position.leverage = (position.notionalUp + position.notionalDown) / position.premium;
        }

        emit BuyDVP(tokenId, _positions[tokenId].expiry, params.notionalUp + params.notionalDown);
        emit Buy(params.dvpAddr, _positions[tokenId].expiry, premium, params.recipient);
    }
\u0060\u0060\u0060

