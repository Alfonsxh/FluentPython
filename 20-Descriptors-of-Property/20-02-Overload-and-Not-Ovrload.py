"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 20-02-Overload-and-Not-Ovrload.py
@time: 18-8-25 下午3:35
@version: v1.0 
"""


# 覆盖型描述符与非覆盖型描述符对比

# 辅助函数，用于显示

def cls_name(obj_or_cls):
    cls = type(obj_or_cls)
    if cls is type:
        cls = obj_or_cls
    return cls.__name__.split(".")[-1]


def display(obj):
    cls = type(obj)
    if cls is type:
        return "<class {}>".format(obj.__name__)  # 如果是类，返回类的描述
    elif cls in [type(None), int]:
        return repr(obj)  # 如果为空或为整数值，则返回对应的描述
    else:
        return "<{} object>".format(cls_name(obj))  # 如果是实例，返回实例描述


def print_args(name, *args):
    """
    打印参数
    :param name: __get__或__set__方法
    :param args: 包括 self(描述符实例), instance(托管类实例), owner(托管类)
    :return:
    """
    pseudo_args = ",".join(display(obj) for obj in args)
    print(
        "-> {cls_name}.__{get_or_set}__({args})".format(cls_name=cls_name(args[0]), get_or_set=name, args=pseudo_args))


# 重要的类

class Overload:
    """覆盖型描述符"""

    def __get__(self, instance, owner):
        print_args("get", self, instance, owner)

    def __set__(self, instance, value):
        print_args("set", self, instance, value)


class OverloadNotGet:
    """没有__get__方法的覆盖型描述符"""

    def __set__(self, instance, value):
        print_args("set", self, instance, value)


class NonOverload:
    """非覆盖型描述符"""

    def __get__(self, instance, owner):
        print_args("get", self, instance, owner)


class Manager:
    override = Overload()
    overrideNonGet = OverloadNotGet()
    nonOverride = NonOverload()

    def test(self):
        print("-> Manager.test({})".format(display(self)))


obj = Manager()
print("\n 覆盖型 __get__ and __set__:")
obj.override  # -> Overload.__get__(<Overload object>,<Manager object>,<class Manager>)
Manager.override  # -> Overload.__get__(<Overload object>,None,<class Manager>)

print("Before set override -> ", obj.__dict__)
obj.override = 7  # -> Overload.__set__(<Overload object>,<Manager object>,7)
obj.override  # -> Overload.__get__(<Overload object>,<Manager object>,<class Manager>)
print("After set override -> ", obj.__dict__)  # {},此时实例中没有override属性

obj.__dict__["override"] = 9  # 通过__dict__给override赋值，不触发__set__方法
print(obj.__dict__)  # {'override': 9},__dict__中含有了override属性
obj.override  # -> Overload.__get__(<Overload object>,<Manager object>,<class Manager>),但取实例属性时，实际上仍取的是类的属性，触发__get__方法

print("\n 无get覆盖型 __get__ and __set__:")
obj.overrideNonGet  # <__main__.OverloadNotGet object at 0x7f0bdd21eba8>, 类未实现__get__方法，直接获取的描述符的实例
Manager.overrideNonGet  # <__main__.OverloadNotGet object at 0x7f0bdd21eba8>

print("Before set overrideNonGet -> ", obj.__dict__)
obj.overrideNonGet = 7  # -> OverloadNotGet.__set__(<OverloadNotGet object>,<Manager object>,7)
print(obj.overrideNonGet)  # <__main__.OverloadNotGet object at 0x7f0bdd21eba8>
print("After set nonOverride -> ", obj.__dict__)

obj.__dict__["overrideNonGet"] = 8
print("obj.overrideNonGet -> ", obj.overrideNonGet)  # obj.overrideNonGet ->  8,overrideNonGet描述符中没有__get__方法，所以不触发，直接返回属性的值

print("\n 非覆盖型 __get__ and __set__:")  # 类没有实现__set__方法时，实例的属性赋值为新建一个属性
obj.nonOverride  # -> NonOverload.__get__(<NonOverload object>,<Manager object>,<class Manager>)
Manager.nonOverride  # -> NonOverload.__get__(<NonOverload object>,None,<class Manager>)
print("Before set nonOverride -> ", obj.__dict__)  # Before set nonOverride ->  {'over': 9, 'overrideNonGet': 8}
obj.nonOverride = 9  # 没有实现__set__方法
print(obj.nonOverride)  # ...取值时不触发__get__方法    # 9
print("After set nonOverride -> ", obj.__dict__)  # After set nonOverride ->  {'over': 9, 'overrideNonGet': 8, 'nonOverride': 9}

print(obj.nonOverride)      # -> 9
Manager.nonOverride  # -> NonOverload.__get__(<NonOverload object>,None,<class Manager>)

print("\n方法是非覆盖型描述符：")
print(obj.test)  # 实例获取的是绑定方法的对象 # <bound method Manager.test of <__main__.Manager object at 0x7f0bdd21ec50>>
print(Manager.test)  # 类获取的是函数  # <function Manager.test at 0x7f0bde8149d8>

