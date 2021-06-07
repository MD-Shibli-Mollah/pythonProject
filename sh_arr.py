from typing import List, Iterator

if __name__ == '__main__':
    n = int(input().strip())
    my_list = []
    # map splits the inputs as spaces (2 3 6 6 5) into single INT -- SYNTAX map(function, iterables)
    nums = map(int, input().split())

    for i in nums:
        my_list.append(i)

    my_list.sort()
    # Dictionary remove any duplicates from the list
    dict_lst = dict.fromkeys(my_list)
    f_lst = list(dict_lst)
    f_len = len(f_lst)
    run_up = f_lst[f_len - 2]
    print(run_up)
