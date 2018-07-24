"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 16-04-AveragerYieldFrom.py
@time: 18-7-24 下午9:47
@version: v1.0 
"""

# yield from 功能二：将最外层的调用方与最内层的子生成器连接起来，使两者间能够直接发送和产生值。

from collections import namedtuple

Result = namedtuple("Result", "count,average")


# 自生成器
def Averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield            # 这里接收的是main函数中send的值
        if term is None:        # 这个判断是必须的，否则会一直循环下去，无法返回
            break
        total += term
        count += 1
        average = total / count
    # raise StopIteration(Result(2, 3)) # yield from会捕获StopIteration的第一个参数当做返回值
    return Result(count, average)       # 子生成器产生的值都直接传给委派生成器的调用方，即main函数


# 委派生成器
def Grouper(results, key):
    while True:
        results[key] = yield from Averager()  # yield from会捕获StopIteration的第一个参数当做返回值，即results[key]=StopIteration[0]


def Report(results):
    for key, values in results.items():
        group, unit = key.split(";")
        print("{:2} {} averaging {:.2f} {}".format(values.count, group, values.average, unit))


# 调用方
def main(data: dict):
    results = {}
    for key, values in data.items():
        group = Grouper(results, key)
        next(group)                 # 预激
        for value in values:
            group.send(value)       # 发送给自生成器的值
        group.send(None)            # 停止信号！
    Report(results)


datas = {
    "girls;kg": [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
    "girls;m": [1.6, 1.5, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
    "boys;kg": [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
    "boys;m": [1.6, 1.5, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43]
}

if __name__ == "__main__":
    main(datas)
