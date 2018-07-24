"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 16-01-Coroutine.py
@time: 18-7-1 下午10:53
@version: v1.0 
"""
import inspect


def simple_coroutine1():
    print("->coroutine start")
    x = yield
    print("->coroutine received:", x)


my_cor1 = simple_coroutine1()
print(inspect.getgeneratorstate(my_cor1))  # 生成器处于GEN_CREATED 等待开始执行状态

print("cor -> ", my_cor1)
print("next(cor) -> ", next(my_cor1))  # 激活协程，也称预激。也可以使用cor.send(None)代替。首次不能直接send(xxx)
print(inspect.getgeneratorstate(my_cor1))  # GEN_SUSPENDED 在yield表达式处暂停

try:
    print("cor.send(12)", my_cor1.send(12))  # send完后，生成器抛出StopIteration异常
except StopIteration:
    print("cor StopIteration!")
print(inspect.getgeneratorstate(my_cor1))  # GEN_CLOSED 执行结束

print("\n\n")


# 先执行yield右边的内容，再执行yield左边的内容。
def simple_coroutine2(a):
    print("-> Started: a = ", a)
    b = yield a
    print("-> Received: b = ", b)
    c = yield a + b
    print("-> Received: c = ", c)


my_cor2 = simple_coroutine2(1)
print("my_cor2 state -> ", inspect.getgeneratorstate(my_cor2))

print("\nmy_cor2 -> ", my_cor2)
print("next(my_cor2) - > ", next(my_cor2))         # 激活， 执行yield a，返回a的值。
print("my_cor2 state -> ", inspect.getgeneratorstate(my_cor2))

print("\n")
print("my_cor2.send(10) - > ", my_cor2.send(10))  # 发送10， 执行 b = yeild，打印 Recevied，执行 yield a + b， 返回 a + b 的结果，断住。
print("my_cor2 state -> ", inspect.getgeneratorstate(my_cor2))
print("\n")

try:
    print("\nmy_cor2.send(21) - > ", my_cor2.send(21))  # 产生StopIteration异常，并不会打印此内容
except StopIteration:
    print("cor StopIteration!")

print("my_cor2 state -> ", inspect.getgeneratorstate(my_cor2))
