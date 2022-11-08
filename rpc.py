from web3 import Web3, HTTPProvider


web3 = Web3(HTTPProvider('http://140.210.195.172:8545'))
receipt = web3.eth.waitForTransactionReceipt("0xf9dc41028514ee6d3675388d3c830f2089e4a62a08c4033d66435e636063e84f")



print(receipt.logs)