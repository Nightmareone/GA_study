# 题目描述
# 给定任一个各位数字不完全相同的4位正整数，如果我们先把4个数字按非递增排序，再按非递减排序，然后用第1个数字减第2个数字，将得到
# 一个新的数字。一直重复这样做，我们很快会停在有“数字黑洞”之称的6174，这个神奇的数字也叫Kaprekar常数。
#
#  例如，我们从6767开始，将得到
#
#  7766 - 6677 = 1089
#  9810 - 0189 = 9621
#  9621 - 1269 = 8352
#  8532 - 2358 = 6174
#  7641 - 1467 = 6174
#  ... ...
#
#  现给定任意4位正整数，请编写程序演示到达黑洞的过程。
#
# 输入描述:
# 输入给出一个(0, 10000)区间内的正整数N。
#
# 输出描述:
# 如果N的4位数字全相等，则在一行内输出“N - N = 0000”；否则将计算的每一步在一行内输出，直到6174作为差出现，输出格式见样例,每行中间没有空行。注意每个数字按4位数格
#  式输出。
#
# 输入例子:
# 6767
#
# 输出例子:
# 7766 - 6677 = 1089
#  9810 - 0189 = 9621
#  9621 - 1269 = 8352
#  8532 - 2358 = 6174
##function-----
def get_kaprekar(num):
    while(True):
        num_list = num.split()
        print(b)
        b = num_list.sort()
        b = ''.join(b)
        c = num_list.sort(reverse = True)
        d = int(b) - int(c)
        print(b + '-' + 'c' + '=' + d)
        num = str(d)
        if(num == '6174'):
            break
##main--------
if __name__ == '__main__':
    num = input()
    num = "".join((lambda x:(x.sort(),x)[1])(list(num)))
    print(num)
    # max_count = num.count(max(num))
    # if(int(num) > 0 and int(num) < 10000):
    #     get_kaprekar(num)
    # elif(max_count == len(num)):
    #     print(num + '-' + num + '= 0000')
    # else:
    #     print(0)
