# задать список студентов с оценками (name scores) и вывести среднюю оценку зная имя студента
if __name__ == '__main__':
    n = int(input())
    sum = 0
    answer = 0
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    srednee = student_marks.setdefault(query_name)
    for i in range(len(srednee)):
        sum += srednee[i]
        answer = sum / len(srednee)
    print('{:.2f}'.format(answer))