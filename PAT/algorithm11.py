##function1
def fun1(a, middle_num):##输入list的值，和中间值
    ##对周围8个点进行计算
    chazhi_list = []#像素点之间差值
    min_list = []##差值的最小值

    # 根据输入list的长度不同，删除不同的中间点
    if(len(a) == 9):
        del a[4]
    elif(len(a) == 4):
        del a[0]
    elif(len(a) == 6):
        del a[]

    list_len = len(a)
    for i in range(list_len):
        for j in range(list_len):
            if(i == j):
                continue
            else:
                chazhi_list.append(abs(a[i] - a[j]))
        print(chazhi_list)
        min_list.append(min(chazhi_list))
        chazhi_list.clear()
    max_num = max(min_list)##绝对值的最大值
    print(min_list)
    ##用中间的点的数值，和周围点数值进行计算
    min_middle = 256##最小值
    for n in a:
        minus_num = abs(n - middle_num)
        if(min_middle > minus_num):
            min_middle = minus_num

    print('MAX:' + str(max_num))
    print('middle:' + str(min_middle))

if __name__ == '__main__':

    a = [100, 20, 32, 43, 51, 64, 73, 82, 95]
    middle_num = 51
    # b = [100, 20, 32, 43, 51, 64,12, 32,43, 43,54]
    # c = [100, 20, 32, 43]
    fun1(a, middle_num)
