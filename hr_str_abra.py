def mutate_string(string, position, character):
    my_l = list(string)

    my_l[position] = character
    my_str = ''.join(my_l)
    return my_str

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)