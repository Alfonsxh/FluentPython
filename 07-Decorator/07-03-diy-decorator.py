#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 07-03-diy-decorator.py
@time: 18-2-28 下午7:59
@version: v1.0 
"""
import time
import functools
from clockdeco_demo import clock_one, clock_two, clock_third


@clock_one
def snooze(seconds):
    """睡一会"""
    time.sleep(seconds)


@clock_one
def factorial(n):
    """求阶乘"""
    return 1 if n < 2 else n * factorial(n - 1)


snooze(.234)
print("snooze.__name__:", snooze.__name__)
print("snooze.__doc__:", snooze.__doc__)  # 输出的是装饰器函数的属性
factorial(10)
print("\n")


@clock_two
def fibonacci(n, m=1):
    """计算斐波那契数列"""
    return n if n < 2 else fibonacci(n - 2) + fibonacci(n - 1)


print("fibonacci(6, 2):", fibonacci(6, 2))
print("fibonacci.__name__:", fibonacci.__name__)
print("fibonacci.__doc__:", fibonacci.__doc__)
print("\n")


@functools.lru_cache()  # 带有缓存方式的装饰器
@clock_two
def fibonacci_two(n):
    """计算斐波那契数列2"""
    return n if n < 2 else fibonacci_two(n - 2) + fibonacci_two(n - 1)


print("fibonacci_two(6):", fibonacci_two(6))
print("fibonacci_two.__name__:", fibonacci_two.__name__)
print("fibonacci_two.__doc__:", fibonacci_two.__doc__)
print("\n")


@functools.lru_cache()
@clock_third(fmt="{func_name}({arg_str}): {result}")
def fibonacci_thrid(n):
    """计算斐波那契数列3"""
    return n if n < 2 else fibonacci_thrid(n - 2) + fibonacci_thrid(n - 1)


print("fibonacci_thrid(6) ->", fibonacci_thrid(6))
