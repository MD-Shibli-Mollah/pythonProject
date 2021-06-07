if __name__ == '__main__':
    n = int(input())
    my_list = []
    my_tup = ()

    int_list = map(int, input().split())

    my_tup = tuple(int_list)
    my_h = hash(my_tup)
    print(my_h)
