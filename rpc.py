from web3 import Web3, HTTPProvider

http_provider_url = ""
tx_hash = ""


web3 = Web3(HTTPProvider(http_provider_url))
receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

print(receipt)