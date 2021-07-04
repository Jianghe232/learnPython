#!/usr/bin/env python3

## 华氏温度转摄氏温度

fahrenheit = 0
while fahrenheit <= 250:
    fahrenheit = int(input("请输入华氏温度（大于250结束程序）:\n"))
    celsius = (fahrenheit - 32) / 1.8
    print("{:5d} {:7.2f}".format(fahrenheit, celsius))
