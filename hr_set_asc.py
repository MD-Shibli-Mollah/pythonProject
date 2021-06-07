na = int(input())
arr1 = list(map(int, input().split()))
nb = int(input())
arr2 = list(map(int, input().split()))

set_1 = set(arr1)
set_2 = set(arr2)
my_set_un = set_1.union(set_2)
my_set_inter = set_1.intersection(set_2)
my_f_set = my_set_un.difference(my_set_inter)
my_list = list(my_f_set)
my_list.sort()
for i in my_list:
    print(i)

#print("\n".join(my_set))
