import sys
##--------------fucntion------------
def checkFun(list):
    ##能被5整除的数字中所有偶数的和
    A1 = 0
    A2 = 0
    A3 = 0
    A4 = 0
    A5 = 0
    for n in list:
        if(n % 5 == 0 and n % 2 == 0):
            A1 += n
    ##将被5除后余1的数字按给出顺序进行交错求和，即计算n1-n2+n3-n4...
    for i, n in enumerate(list):
        if(n % 5 == 1 and i % 2 == 1):
            n = -1 * n
        A2 += n
    ##被5除后余2的数字的个数
    for n in list:
        if(n % 5 == 2):
            A3 += 1
    ##被5除后余3的数字的平均数，精确到小数点后1位
    A4 = 0
    a4_amount = 0
    for n in list:
        if(n % 5 == 3):
            a4_amount += 1
            A4 += n
    if(a4_amount == 0):
        A4 = a4_amount
    else:
        A4 = A4 / a4_amount
        A4 = round(A4, 1)
    ##被5除后余4的数字中最大数字
    for n in list:
        if(n % 5 == 4 and A5 < n):
            A5 = n
    print(A1, A2, A3, A4, A5)
##---------------main--------------
option = input()
option = int(option)
list = []
for n in sys.stdin.readline().split():
    n = int(n)
    list.append(n)
if(len(list) != option):
    print("N")
else:
    checkFun(list)
