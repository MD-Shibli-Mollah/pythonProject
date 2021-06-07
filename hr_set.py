def average(array):
    my_set = set(array)
    my_cnt = len(my_set)
    avg = sum(my_set) / my_cnt
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
