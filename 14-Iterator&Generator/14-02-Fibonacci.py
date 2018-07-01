"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 14-01-Sentence.py
@time: 18-7-1 下午9:45
@version: v1.0 
"""


# 斐波那契数列复杂实现
class Fibonacci:
    def __iter__(self):
        return FibonacciIterator()


class FibonacciIterator:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result

    def __iter__(self):
        return self


# 斐波那契数列Python实现
def FibonacciFunc():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, b + 1
