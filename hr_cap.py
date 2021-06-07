def my_cap(s):
    for i in s.split():
        cap = i.capitalize()
        s = s.replace(i, cap)

    # my_sp = s.find(" ") +1
    # my_l = list(s)
    # my_l[0] = my_l[0].upper()
    # my_l[my_sp] = my_l[my_sp].upper()
    # my_str = "".join(my_l)
    print(s)
    return


if __name__ == '__main__':
    s = input()
    my_cap(s)
