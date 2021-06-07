my_in = int(input())
print(my_in)
for i in range(1, my_in + 1):
    inpa = input()
    my_set1 = set(map(int, input().split()))
    inpb = input()
    my_set2 = set(map(int, input().split()))
    print(my_set1.issubset(my_set2))
