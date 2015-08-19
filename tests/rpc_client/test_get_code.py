from populus.client import Client


def test_get_code(rpc_server, eth_tester):
    client = Client('127.0.0.1', '8545')

    data = "0x606060405260f8806100126000396000f30060606040526000357c01000000000000000000000000000000000000000000000000000000009004806316216f3914604b578063a5f3c23b14606a578063dcf537b1146095576049565b005b605460045060e6565b6040518082815260200191505060405180910390f35b607f60048035906020018035906020015060ba565b6040518082815260200191505060405180910390f35b60a460048035906020015060d0565b6040518082815260200191505060405180910390f35b60008183019050805080905060ca565b92915050565b6000600782029050805080905060e1565b919050565b6000600d9050805080905060f5565b9056"
    from_addr = eth_tester.encode_hex(eth_tester.accounts[0])

    txn_hash = client.send_transaction(
        _from=from_addr,
        data=data,
    )
    txn_receipt = client.get_transaction_receipt(txn_hash)
    contract_addr = txn_receipt['contractAddress']

    code = client.get_code(contract_addr)
    # TODO: figure out what's going on here and why the two are almost the same
    # but not exactly the same.
    assert len(code) > 100
    assert data.endswith(code[2:])
