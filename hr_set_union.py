inpa = input()
my_set1 = set(map(int, input().split()))

inpb = input()
my_set2 = set(map(int, input().split()))

my_s = my_set1.union(my_set2)
my_s = my_set1.symmetric_difference(my_set2)
print(len(my_s))
