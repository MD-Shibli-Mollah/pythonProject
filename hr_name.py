def print_full_name(a, b):

    str1 = "Hello %s " %(a)
    str2 = "%s! You just delved into python." %(b)
    str = str1+str2
    print(str)

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)