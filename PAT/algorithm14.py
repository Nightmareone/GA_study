if __name__ == "__main__":
    option = input()
    option = int(option)
    graph = []
    array = []
    for n in range(option):
        input_str = input()
        str_split = input_str.split(" ")
        if(str_split[1] > "1814/09/06" or str_split[1] < "2014/09/06"):
            print(str_split[1])
            array.append(str_split[1])
            graph.append(str_split[0])

    eldest = min(array)
    num_eldest = array.index(eldest)
    youngest = max(array)
    num_youngest = array.index(youngest)
    print("-----------------------------")
    print(len(array), graph[num_eldest], graph[num_youngest])
