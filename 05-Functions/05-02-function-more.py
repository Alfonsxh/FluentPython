#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 05-02-function-more.py
@time: 18-2-9 下午9:58
@version: v1.0 
"""
# python可调用对象
print("*" * 32 + "python可调用对象" + "*" * 32)
print("""用户定义的函数
        使用 def 语句或 lambda 表达式创建。
内置函数
        使用 C 语言(CPython)实现的函数,如 len 或 time.strftime。
内置方法
        使用 C 语言实现的方法,如 dict.get。
方法
        在类的定义体中定义的函数。
类
        调用类时会运行类的 __new__ 方法创建一个实例,然后运行
        __init__ 方法,初始化实例,最后把实例返回给调用方。因为 Python
        没有 new 运算符,所以调用类相当于调用函数。(通常,调用类会创建
        那个类的实例,不过覆盖 __new__ 方法的话,也可能出现其他行为。
        19.1.3 节会见到一个例子。)
类的实例
        如果类定义了 __call__ 方法,那么它的实例可以作为函数调用。
""")
print('\n' * 2)
print("abs, str, 123:".rjust(30), abs, str, 123)
print("callable(obj) ".rjust(30), [callable(obj) for obj in [abs, str, 123]])  # callable(obj) 可以判断对象是否可以被调用
print('\n' * 2)

# 类类型调用
print("*" * 32 + "类类型调用" + "*" * 32)
import random


class BingoCage:
    def __init__(self, item):
        self._items = list(item)
        random.shuffle(self._items)  # shuffle() 方法将序列的所有元素随机排序

    def pick(self):
        try:
            return self._items.pop()
        except:
            raise LookupError("pick from empty.")

    def __call__(self, *args, **kwargs):
        return self.pick()


bingo = BingoCage(range(5))
print("bingo.pick():".rjust(30), bingo.pick())
print("bingo():".rjust(30), bingo())  # 调用__call__方法
print("callable(bingo):".rjust(30), callable(bingo))
print('\n' * 2)

# 函数与类的属性
print("*" * 32 + "函数与类的属性" + "*" * 32)


class C:
    pass


def func(): pass


obj = C()
print("dir(class):".rjust(30), sorted(dir(obj)))
print("dir(function):".rjust(30), sorted(dir(func)))
print("set(dir(func)) - set(dir(obj)):".rjust(30), sorted(set(dir(func)) - set(dir(obj))))
print("set(dir(obj)) - set(dir(func)):".rjust(30), set(dir(obj)) - set(dir(func)))
print('\n' * 2)

# 仅限关键字(keyword-only argument)
print("*" * 32 + "仅限关键字(keyword-only argument)" + "*" * 32)

print(":".rjust(30), )
print("*" * 32 + "" + "*" * 32)
