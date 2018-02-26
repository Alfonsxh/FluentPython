#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 07-01-decorator.py
@time: 18-2-26 下午9:27
@version: v1.0 
"""
# python 装饰器
# 1.能把被装饰的函数替换成其他函数。
# 2.装饰器在加载模块时立即执行。
print("*" * 32 + "python 装饰器" + "*" * 32)

registry_list = []


def registry(func):
    print("Running registry(%s)" % func)
    registry_list.append(func)
    return func


@registry
def func1():
    print("Running func1()")


@registry
def func2():
    print("Running func2()")


def func3():
    print("Running func3()")


def main():
    print("Running main()")
    print("registry_list: %s" % registry_list)
    func1()
    func2()
    func3()


if __name__ == "__main__":
    main()
