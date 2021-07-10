#!/bin/env python3


# 判断学生成绩是否达标的程序，要求输入学生数量，以及各个学生物理、数学、历史三科的成绩，如果总成绩小于 120，程序打印 “failed”，否则打印 “passed”。


n = int(input("Enter the number of students: "))
data = {}   # 存储数据的字典变量
Subjects = ('Physics', 'Math', 'History')
for num in range(0, n):
    name = input('Enter the name of the student {}: '.format(num + 1)) # 获得学生姓名
    marks = [] # 存储学生每一科的分数
    for x in Subjects:
        marks.append(int(input("Enter the marks of the {}: ".format(x)))) # 获得每一科的分数
    data[name] = marks

for x, y in data.items():
    total = sum(y)
    print("{}'s total marks {}".format(x,total))
    if total < 120:
        print(x, "failed :(")
    else:
        print(x, "passed :)")
