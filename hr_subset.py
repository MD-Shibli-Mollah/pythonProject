my_set1 = set(map(int, input().split()))
my_in = int(input())
for i in range(1, my_in + 1):
    inpb = input()
    my_set2 = set(map(int, input().split()))
    print(my_set1.issubset(my_set2))
