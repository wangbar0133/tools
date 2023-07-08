import os
import sys
from web3 import Web3

if __name__ == "__main__":
    address = sys.argv[1]
    slot_loc = sys.argv[2]
    GETHAPI = sys.argv[3]

    # 初始化Web3对象
    w3 = Web3(Web3.HTTPProvider(GETHAPI))

    # 读取slot
    value = w3.eth.getStorageAt(address, slot_loc).hex()

    print("hex:  " + value)
    print("int:  " + int(value, 16).__str__())