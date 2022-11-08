from web3.auto import w3
from web3 import Web3
from eth_account.messages import encode_defunct, _hash_eip191_message


def to_32byte_hex(val):
    return Web3.toHex(Web3.toBytes(val).rjust(32, b'\0'))


private_key = '0x7bb22bc28680d0b414a7affb8ff9059291524611ab54f336f985a8ef2c5b6e77'

hex_message = ''

message = encode_defunct(hexstr=hex_message)

_hash = "0x7c9830d7479756cbc3c70f0441c4ba902d66f4587f27edce9ef0e260aa61897b"

sign = w3.eth.account.signHash(_hash, private_key=private_key)

print("h: {}", Web3.toHex(sign.messageHash))
print("v: {}", sign.v)
print("r; {}", to_32byte_hex(sign.r))
print("s: {}", to_32byte_hex(sign.s))

ad = w3.eth.account.recoverHash(_hash, signature=sign.signature)
print(ad)

