##function--------------
def function(alist):
    n = len(alist)
    for j in range(n - 1):
        count = 0
        for i in range(0, n - 1 - j):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                count += 1
        if 0 == count:
            break
    return alist

#main-------------------
if __name__ == '__main__':
    input_data = input().split()
    the_raw_data = []
    count_nums = -1
    for i,n in enumerate(input_data):
        count_nums += 1
        n = int(n)
        for j in range(n):
            the_raw_data += str(count_nums)

    result = function(the_raw_data)
    if(result[0] == '0'):
        for i, n in enumerate(result):
            if(result[i] > result[0]):
                result[0], result[i] = result[i], result[0]
                break
    print(''.join(result))
