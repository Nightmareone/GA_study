#-------------------------
#福尔摩斯的约会
#-------------------------
import re
##内容处理函数-
def get_the_time(str1, str2, str3, str4):
    list_str1 = list(str1)
    list_str2 = list(str2)
    list_str3 = list(str3)
    list_str4 = list(str4)

    ##确定对比的两串字符数组中长度最短的那个，以最短这个数值最为接下来循环边界
    max_compare1 = 0
    max_compare2 = 0
    if(len(list_str1) < len(list_str2)):
        max_compare1 =  len(list_str1)
    else:
        max_compare1 =  len(list_str2)

    if(len(list_str3) < len(list_str4)):
        max_compare2 =  len(list_str3)
    else:
        max_compare2 =  len(list_str3)

    ##进行循环对比,获取最终的结果
    ##MON表示星期一，TUE表示星期二，WED表示星期三，THU表示星期四，FRI表示星期五，SAT表示星期六，SUN表示星期日
    ##获得星期几-----------------------
    dateGet = ""
    count = 0
    for n in range(max_compare1):
        if(list_str1[n] == list_str2[n]):
            pattern = re.compile(r"[A-G]")
            match = pattern.match(list_str1[n])
            if(match):
                dateGet = match.group()
        count += 1
    print(count)
    ##获得小时数----------------------
    # for n in range(count, max_compare1):

    ##获得分钟数----------------------
    minute_count2 = -1
    for n in range(max_compare2):
        minute_count2 += 1
        if(list_str3[n] == list_str4[n]):
            pattern = re.compile(r"[a-z]")
            match = pattern.match(list_str1[n])
            if(match):
                break
    if(minute_count2 < 10):
        minute_count2 = "0" + str(minute_count2)
    ##获得最终的结果----------------------
    dict_date = {"A": "MON", "B" : "TUE","C" : "WED", "D": "THU", "E": "FRI", "F": "SAT", "G": "SUN"}
    val = dict_date[dateGet]
    print(dateGet)
    print(val)
    # hour = ord(list_count[1]) - ord('A') + 10
    # print(hour)

    # content = str(val) + " " + str(hour) + ":" + str(minute_count2)
    # return content

##主函数
# str1 = input()
# str2 = input()
# str3 = input()
# str4 = input()
str1 = "3485djDkxh4hhGE"
str2 = "2984akDfkkkkggEdsb"
str3 = "s&hgsfdk"
str4 = "d&Hyscvnm"
# result = get_the_time(str1, str2, str3, str4)
# print(result)
get_the_time(str1, str2, str3, str4)
