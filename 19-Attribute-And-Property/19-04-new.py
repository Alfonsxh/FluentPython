"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 19-04-new.py
@time: 18-8-16 下午10:44
@version: v1.0 
"""


# __new__方法介绍：https://www.cnblogs.com/ifantastic/p/3175735.html

# __new__ 是类的一个方法，在实例化类时，在调用__init__之前，会调用__new__方法。
# - 通常来说，新式类开始实例化时，__new__()方法会返回cls（cls指代当前类）的实例，
#   然后该类的__init__()方法作为构造方法会接收这个实例（即self）作为自己的第一个参数，
#   然后依次传入__new__()方法中接收的位置参数和命名参数。

# ---------------------------------------例一--------------------------------------------
class Foo(object):
    def __new__(cls, x, *args, **kwargs):
        self = object.__new__(cls)  # 实例化需先调用父类的实例化方法__new__
        self.x = x
        return self

    def __init__(self, *args, **kwargs):  # 初始化方法，self中已经添加了属性x
        print("vars(self) -> ", vars(self))
        self.args = args
        self.kwargs = kwargs


foo = Foo(10, "hello", kwargs="world")
print(foo.x, foo.args, foo.kwargs)
print(foo.__dict__)


class Bar(Foo):

    def __init__(self, *args, **kwargs):
        self.bar_args = args
        self.bar_kwargs = kwargs


bar = Bar(10, "hello", kwargs="world")  # 使用父类Foo的__new__方法实例化，self中含有x属性
print("\n", bar.x, bar.bar_args, bar.bar_kwargs)
print(bar.__dict__)  # 子类Bar中的__init__方法替换了父类Foo中的初始化方法，是的子类的__dict__不含有key值args、kwargs


# ---------------------------------------例二--------------------------------------------

class Foo1(object):
    def __new__(cls, *args, **kwargs):
        self = object.__new__(cls)  # 将属性在__new__方法中赋值
        self.x = args[0]
        self.args = args
        self.kwargs = kwargs
        return self


foo1 = Foo1(10, "hello", kwargs="world")
print("\n", foo1.x, foo1.args, foo1.kwargs)
print(foo1.__dict__)


class Bar1(Foo1):

    def __init__(self, *args, **kwargs):  # 此时继承父类Foo1，由于父类没有__init__方法，所以会多出属性args和kwargs
        self.bar_args = args
        self.bar_kwargs = kwargs


bar1 = Bar1(10, "hello", kwargs="world")
print("\n", bar1.x, bar1.bar_args, bar1.bar_kwargs)
print(bar1.__dict__)


# ---------------------------------------例三--------------------------------------------

class Foo2(object):
    def __init__(self, *args, **kwargs):  # Foo2中没有__new__方法，类的属性均在__init__方法中赋值
        self.x = args[0]
        self.args = args
        self.kwargs = kwargs


foo2 = Foo2(10, "hello", kwargs="world")
print("\n", foo2.x, foo2.args, foo2.kwargs)
print(foo2.__dict__)


class Bar2(Foo2):
    def __init__(self, *args, **kwargs):  # Bar2类，重载了父类的__init__方法，使得父类的属性x、args、kwargs在子类中不存在了
        self.bar_args = args
        self.bar_kwargs = kwargs


bar2 = Bar2(10, "hello", kwargs="world")
# print("\n", bar2.x, bar2.bar_args, bar2.bar_kwargs)       # bar2.x不存在了
print("\n", bar2.bar_args, bar2.bar_kwargs)
print(bar2.__dict__)
