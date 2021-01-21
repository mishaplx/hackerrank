'''Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.'''
'''
from itertools import groupby

n = int(input())
python_student = []
x = 0
while x != n:
    name = input("enter name: ")
    school_grade = float(input("enter school grade: "))
    x += 1
    for j in range(n):
        a2 = []
        a2.append(name)
        a2.append(school_grade)
        python_student.append(a2)
python_student = [el for el, _ in groupby(python_student)]
python_student.sort()
print(python_student)
'''
n=int(input())
arr=[[input("name: "),float(input("grade: "))] for _ in range(0,n)]
print(arr)