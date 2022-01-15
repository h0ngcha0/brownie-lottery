from brownie import Lottery, accounts, config, network
from web3 import Web3

def test_get_entry_fee():
    account = accounts[0]
    lottery = Lottery.deploy(config["networks"][network.show_active()]["eth_usd_price_feed"], {"from": account})
    fee = lottery.getEntranceFee()
    print(f"fee: {fee}")
    assert fee > Web3.toWei(0.01, "ether")
    assert fee < Web3.toWei(0.05, "ether")
