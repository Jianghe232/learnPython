#!/usr/bin/env python3

## 计算 10 个数字的平均值

N = 10
sum = 0
count = 0
while count < N:
    print("请输入第{}个数字".format(count + 1))
    number = float(input())
    sum += number
#    count++    python 中没有++ --
    count += 1
average = sum / N
print("这 10 个数字的和为:{},平均值为:{:.2f}".format(sum,average))
