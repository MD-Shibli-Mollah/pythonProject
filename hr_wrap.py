import textwrap


def wrap(my_string, max_width):
    my_wrap = textwrap.wrap(my_string, max_width)
    return "\n".join(my_wrap)

if __name__ == '__main__':
    my_string, max_width = str(input()), int(input())
    result = wrap(my_string, max_width)
    print(result)
