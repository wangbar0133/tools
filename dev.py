from web3 import Web3

w3 = Web3(Web3.HTTPProvider('http://140.210.217.225:8545/'))
account = w3.eth.account.from_key(
    "0x7bb22bc28680d0b414a7affb8ff9059291524611ab54f336f985a8ef2c5b6e77")

abi = [
	
]




with open('bytecode.txt', 'r') as f:
    code = f.read()

bytecode = code

contract = w3.eth.contract(abi=abi, bytecode=bytecode)

construct_txn = contract.constructor().buildTransaction({
    'from': account.address,
    'nonce': w3.eth.getTransactionCount(account.address),
    'gas': 5000000,
    'gasPrice': w3.toWei('21', 'gwei')
    }
)

signed = account.signTransaction(construct_txn)

tx_id = w3.eth.sendRawTransaction(signed.rawTransaction)
receipt = w3.eth.waitForTransactionReceipt(tx_id)
address = receipt.contractAddress
print(address)




