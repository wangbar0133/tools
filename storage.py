import os
import sys
from web3 import Web3

if __name__ == "__main__":
    address = sys.argv[1]
    slot_loc = sys.argv[2]
    GETHAPI = sys.argv[3]

    # init Web3 object
    w3 = Web3(Web3.HTTPProvider(GETHAPI))

    # read slot
    value = w3.eth.get_storage_at(address, slot_loc).hex()

    print("hex:  " + value)
    print("int:  " + int(value, 16).__str__())