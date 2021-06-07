na = int(input())
my_set = set()
for i in range(1, na + 1):
    my_country = input()
    my_set.add(my_country)
print(len(my_set))
# print(len({input() for x in range(int(input()))}))