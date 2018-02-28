#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: clockdeco_demo.py
@time: 18-2-28 下午7:53
@version: v1.0 
"""
import time


def clock_one(func):  # 一般的装饰器实现
    """计时装饰器1"""

    def clocked(*args):
        """计时函数"""
        start_time = time.time()
        result = func(*args)
        total_time = time.time() - start_time
        func_name = func.__name__
        arg_str = ",".join(repr(arg) for arg in args)
        print("[%0.8fs] %s(%s) -> %r" % (total_time, func_name, arg_str, result))
        return result

    return clocked


from functools import wraps


def clock_two(func):  # 将func本身的属性返回的装饰器实现
    """计时装饰器2"""

    @wraps(func)  # 将func本身的属性返回(__name__、__doc__等等)
    def clocked(*args, **kwargs):
        """计时函数"""
        start_time = time.time()
        result = func(*args, **kwargs)
        total_time = time.time() - start_time
        func_name = func.__name__
        args_lst = []
        if args:
            args_lst += [repr(arg) for arg in args]
        if kwargs:
            args_lst += ["%s = %s" % (k, w) for (k, w) in sorted(kwargs.items())]
        arg_str = ",".join(args_lst)
        print("[%0.8fs] %s(%s) -> %r" % (total_time, func_name, arg_str, result))
        return result

    return clocked


# 自定义输出格式的计时装饰器
DEFAULT_FMT = "[{total_time:0.8f}s] {func_name}({arg_str}) -> {result}"


def clock_third(fmt=DEFAULT_FMT):
    def decorator(func):

        @wraps(func)  # 将func本身的属性返回(__name__、__doc__等等)
        def clocked(*args, **kwargs):
            """计时函数"""
            start_time = time.time()
            result = func(*args, **kwargs)
            total_time = time.time() - start_time
            func_name = func.__name__
            args_lst = []
            if args:
                args_lst += [repr(arg) for arg in args]
            if kwargs:
                args_lst += ["%s = %s" % (k, w) for (k, w) in sorted(kwargs.items())]
            arg_str = ",".join(args_lst)
            print(fmt.format(**locals()))
            return result

        return clocked

    return decorator
