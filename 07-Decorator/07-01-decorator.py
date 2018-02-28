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
# 3.装饰器的强大在于它能够在不修改原有业务逻辑的情况下对代码进行扩展，
#   权限校验、用户认证、日志记录、性能测试、事务处理、缓存等都是装饰器的绝佳应用场景，
#   能够最大程度地对代码进行复用。
print("*" * 32 + "python 装饰器" + "*" * 32)

registry_list = []


def func_cheat():
    print("Running cheat.")


def registry(func):
    print("Running registry(%s)" % func)
    registry_list.append(func)
    return func_cheat if func.__name__ == "func1" else func


@registry  # 装饰器在加载模块时立即执行
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
    func1()  # 把被装饰的函数替换成其他函数
    func2()
    func3()


if __name__ == "__main__":
    main()

# python 装饰器进阶
print("*" * 32 + "python 装饰器进阶" + "*" * 32)


def use_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                print("WARN: running %s" % func.__name__)
            elif level == "debug":
                print("DEBUG: running %s" % func.__name__)
            func(*args, **kwargs)

        return wrapper

    return decorator


@use_logging(level = "debug")
def func4(name = "func4"):
    print("name is %s " % name)


func4("tom")

# python 类装饰器
print("*" * 32 + "python 类装饰器" + "*" * 32)


class FuncClass:
    def __init__(self, func):
        self._func = func

    def __call__(self):
        print("Running self.__call__")
        self._func()


@FuncClass
def func5():
    print("Running func5.")


func5()
