
if __name__ == '__main__':
    # n = int(input().strip())
    list = [[1, 5], [2, 3], [3, 4], [4, 2]]
    # lambda is used for sorting with 2nd element of the list
    my_srt = sorted(list, key=lambda x: x[1])
    print(my_srt)

    n = 3
    for i in range(0, n+1):
        print(i)
    # i = 1
    # f_lst = []
    # Here 1 is the
    # for i in range(1, lst_len + 1):
    #     if lst[i - 1] == lst[lst_len]:
    #         lst.pop()
    #     elif lst[i - 1] != lst[lst_len]:
    #         f_lst.append(lst[i - 1])
    # print(f_lst)

    # i = 1
    # -----------end help to print in one line without space----------
    # while i <= n:
    #     print(i, end='')
    #     i += 1

# def is_leap(year):
#     leap = False
#
#     # Write your logic here
#     if (year % 4) == 0 and ((year % 100) != 0 or (year % 400) == 0):
#         leap = True
#     return leap
# year = int(input())
# print(is_leap(year))
