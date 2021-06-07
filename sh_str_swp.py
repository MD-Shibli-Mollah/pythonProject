def swap_case(s):
    my_str = ""
    for i in s:
        if i.isupper():
            j = i
            j = j.lower()
            my_str = my_str + j
            j = ""
        if i.islower():
            j = i
            j = j.upper()
            my_str = my_str + j
            j = ""
        if not i.islower() and not i.isupper():
            my_str = my_str + i
    return my_str


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
