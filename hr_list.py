if __name__ == '__main__':
    my_list = []
    n = int(input())
    for i in range(0, n):
        my_inp = input()
        my_val = my_inp.split()
        if my_val[0] == "insert":
            my_list.insert(int(my_val[1]), int(my_val[2]))
        if my_val[0] == "print":
            print(my_list)
        if my_val[0] == "remove":
            my_list.remove(int(my_val[1]))
        if my_val[0] == "append":
            my_list.append(int(my_val[1]))
        if my_val[0] == "sort":
            my_list.sort()
        if my_val[0] == "pop":
            my_list.pop()
        if my_val[0] == "reverse":
            my_list.reverse()
