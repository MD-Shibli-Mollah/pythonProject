

n = int(input().strip())
matrix = []
# set/dict function eliminates any duplications
scores = set()
for i in range(n):
    name = input()
    score = float(input())
    # Append an empty sublist inside the list
    matrix.append([])
    scores.add(score)

    for j in range(1):
        matrix[i].append(name)
        matrix[i].append(score)

# print(matrix)
# print(scores)

my_srt_set = sorted(scores)

my_2nd_low = my_srt_set[1]
second_low_name = []
# print(my_2nd_low)
for name, scr in matrix:
    if my_2nd_low == scr:
        second_low_name.append(name)

for i in sorted(second_low_name):
    print(i)
