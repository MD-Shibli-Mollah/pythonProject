if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    q_list = student_marks[query_name]

    sum = 0
    ls_len = len(q_list)
    for i in q_list:
        sum = sum + i

    avg = sum/ls_len
    print('%.2f' % avg)