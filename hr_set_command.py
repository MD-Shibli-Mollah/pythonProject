inp = input()
my_set = set(map(int, input().split()))

no_of_commands = int(input())
for i in range(1, no_of_commands + 1):
    my_command = input()
    my_com = my_command.split()
    com = (my_com[0])
    if com == "pop":
        my_set.pop()
    if com == "remove":
        com_val = int(my_com[1])
        my_set.remove(com_val)
    if com == "discard":
        com_val = int(my_com[1])
        my_set.discard(com_val)
print(sum(my_set))
