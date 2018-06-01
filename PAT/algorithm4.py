import sys
##判断是否为质数
def checkFun(num):
    for n in range(2, num):
        if(num % n == 0):
            return -1
    return num
##主函数
min,max =  sys.stdin.readline().split()
min = int(min)
max = int(max)
list = []
result = []
for n in range(2 , 10001):
    if(checkFun(n) != -1):
        list.append(n)

for i, n in enumerate(list):
    if((i+1) >= min and (i+1) <= max):
        result.append(n)

for i, n in enumerate(result):
    if((i + 1) % 10 != 0):
        print(n, end = " ")
    elif(i + 1 == len(result)):
        print(n, end = "")
    else:
        print(n)
