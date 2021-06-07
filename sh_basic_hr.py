import os


def decryptPassword(s):
    my_list = list(s)
    str_list = len(my_list)

    for i in range(0, str_list - 1):
        if str.islower(my_list[i]) and str.isupper(my_list[i + 1]):
            my_list[i], my_list[i + 1] = my_list[i+1], my_list[i]
            my_list[i+2] = "*"
            str_list = str_list + 1
    # --------convert list to string ---------------
    my_str = ''
    for ele in my_list:
        my_str += ele
    print(my_str)
    return


if __name__ == '__main__':
    #    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = decryptPassword(s)

    # fptr.write(result + '\n')
    #
    # fptr.close()
