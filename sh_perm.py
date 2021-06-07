
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    # output_list = [output_exp for var in input_list if (var satisfies this condition)]
    out_pt = [[i, j, k] for i in range(0, x + 1) for j in range(0, y + 1) for k in range(0, z + 1) if ((i + j + k) != n)]

    print(out_pt)
