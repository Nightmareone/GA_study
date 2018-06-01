# NowCoder数列
# 时间限制 3000 ms 内存限制 32768 KB 代码长度限制 100 KB 判断程序 Standard (来自 小小)
# 题目描述
# NowCoder最近在研究一个数列：
#
# * F(0) = 7
# * F(1) = 11
# * F(n) = F(n-1) + F(n-2) (n≥2)
#
# 他称之为NowCoder数列。请你帮忙确认一下数列中第n个数是否是3的倍数。
#
# 输入描述:
# 输入包含多组数据。
# 每组数据包含一个整数n，(0≤n≤1000000)。
#
#
# 输出描述:
# 对应每一组输入有一行输出。
#
# 如果F(n)是3的倍数，则输出“Yes”；否则输出“No”。
#
# 输入例子:
# 0
# 1
# 2
# 3
# 4
# 5
#
# 输出例子:
# No
# No
# Yes
# No
# No
# No
import sys
import re
##NowCoder数列实现函数
def nowcoder(input):
    if(input % 4 == 2):
        return "Yes"
    else:
        return "No"
##主函数
if __name__ == '__main__':
    num = 0
    for n in sys.stdin.readlines():
        num = int(n)
        print(nowcoder(num))
