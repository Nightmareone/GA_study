## beginn to do the choice
def check(a,b,c):
    min = -2 ** 31
    max = 2 ** 31
    if(a < min or a > max or b < min or b > max or c < min or c > max):
        return "false"
    else:
        if(a + b > c):
            return "true"
        else:
            return "false"

## get the input
option = input()
option = int(option)
list = []
for n in range(option):
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    info = check(a,b,c)
    list.append("Case #" + str(n+1) + ": " + str(info))

for info in list:
    print(info)
