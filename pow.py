import hashlib


for num in range(10000,9999999999):
    res = hashlib.sha256(b'iDjT6WLv'+str(num).encode()).hexdigest() #sha1改为题目需要的算法
    b=bin(int(res,16))[2:]
    # print(b)
    if str(b).endswith("0000000000000000000"):
        print(str(num))
        break
    # if res[0:6] == "000000":   #对hash的前五位为"903ed"的数字进行碰撞
    #     print(str(num)) #等待执行结束 输出结果
    #     break