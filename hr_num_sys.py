def print_formatted(number):
    # define padding with pad
    pad = number.bit_length()

    for i in range(1, number + 1):
        my_int = str(i)
        my_int = my_int.rjust(pad)
        my_oct = oct(i)
        my_oct = my_oct[2:].rjust(pad)
        my_hex = hex(i)
        my_hex = my_hex[2:].upper().rjust(pad)
        my_bin = bin(i)
        my_bin = my_bin[2:].rjust(pad)
        print(my_int, my_oct, my_hex, my_bin)
        # print(f'{i:{pad}d} {i:{pad}o} {i:{pad}X} {i:{pad}b}')
    return


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
