##function-----------------------------
def positional_notation(amount, num3):
    array = []
    result = []
    while(True):
        yu = amount % num3
        shang = amount // num3
        amount = shang
        array.append(yu)
        if(shang == 0):
            break
    for n in range(len(array)):
        result.append(change_to_sixteen(array.pop()))
    print("".join(result))

def change_to_sixteen(a):
    if(a > 9):
        sixteen_array = ['A', 'B', 'C', 'D', 'E', 'F']
        num = a - 10
        return sixteen_array[num]
    else:
        return str(a)
##main--------------------------------
if __name__ == '__main__':
    A,B,D = input().split()
    A = int(A)
    B = int(B)
    D = int(D)
    amount = A + B
    positional_notation(amount, D)
