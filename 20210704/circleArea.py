#!/bin/env python3


## 计算圆的面积

import math
r = 1
while r:
    r = int(input("请输入圆的半径（输入 0 退出程序）："))
    if r == 0:
        print("再见！")
        break
    print ("半径为{}的圆面积为：{:.10f}".format(r, r ** 2 * math.pi))
