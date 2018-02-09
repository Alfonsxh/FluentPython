#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 05-01-super-functions.py
@time: 18-2-9 下午9:18
@version: v1.0 
"""
# 函数对象
print("*" * 32 + "函数对象" + "*" * 32)


def factorial(n):
    """return n!"""
    return 1 if n < 2 else n * factorial(n - 1)


print("factorial(10):".rjust(30), factorial(10))
print("factorial.__doc__:".rjust(30), factorial.__doc__)
print("type(factorial):".rjust(30), type(factorial))
fact = factorial
print("fact:".rjust(30), fact)
print("fact(10):".rjust(30), fact(10))
print("map(fact, range(10))".rjust(30), map(fact, range(10)))
print("list(map(fact, range(10)))".rjust(30), list(map(fact, range(10))))
print('\n' * 2)

# 高阶函数：接受函数作为参数，或者把函数当做结果返回的函数。
print("*" * 32 + "高阶函数" + "*" * 32)


# 反向排序
def reverse(word):
    return word[::-1]


fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print("sorted(%s, key=reverse):".rjust(30) % fruits, sorted(fruits, key=reverse))
print('\n' * 2)

# map、filter、reduce的使用及替代方案
print("*" * 32 + "map、filter、reduce的使用及替代方案" + "*" * 32)
print("map(function, sequence) ：".rjust(43), "对sequence中的item依次执行function(item)，将执行结果组成一个List返回。")
print("filter(function, sequence)：".rjust(43),
      "对sequence中的item依次执行function(item)，将执行结果为True的item组成一个List/String/Tuple（取决于sequence的类型）返回。")
print("reduce(function, sequence, starting_value)：".rjust(43),
      "对sequence中的item顺序迭代调用function，如果有starting_value，还可以作为初始值调用，例如可以用来对List求和。")
print("list(map(factorial, range(11))):".rjust(30), list(map(factorial, range(11))))
print("list(factorial(i) for i in range(11)):".rjust(30), list(factorial(i) for i in range(11)))
print("list(map(factorial, filter(lambda n: n % 2, range(11)))):".rjust(30),
      list(map(factorial, filter(lambda n: n % 2 != 0, range(11)))))
print("list(factorial(i) for i in range(11) if i % 2):".rjust(30), list(factorial(i) for i in range(11) if i % 2 != 0))

from functools import reduce
from operator import add

# 1 + 2 + 3 +…… + 99 = ?
print("reduce(add, range(100)):".rjust(30), reduce(add, range(100)))
print("sum(range(100)):".rjust(30), sum(range(100)))
print("\n" * 2)

# lambda表达式
print("*" * 32 + "lambda表达式" + "*" * 32)
print("sorted(fruits, key=lambda word: word[::-1]):".rjust(30), sorted(fruits, key=lambda word: word[::-1]))
