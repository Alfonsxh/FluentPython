"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 21-02-Class-Decorator.py
@time: 18-9-2 上午11:56
@version: v1.0 
"""
import abc


class AutoStorage:
    __counter = 0

    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = cls.__counter
        self.storage_name = "_{classname}#{index}".format(classname=prefix, index=index)
        cls.__counter += 1

    def __get__(self, instance, owner):
        """
        获取描述符属性的值
        :param instance: 托管类实例
        :param owner: 托管类的引用
        :return: 描述符的属性值
        """
        if instance is None:
            return self
        else:
            return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        """
        设置描述符的属性的值
        :param instance: 托管类的实例
        :param value: 需要设置的值
        :return:
        """
        setattr(instance, self.storage_name, value)  # 在托管实例的字典表中添加对应的属性值


class Validated(abc.ABC, AutoStorage):  # 属性值验证类
    def __set__(self, instance, value):
        value = self.Validate(instance, value)
        super().__set__(instance, value)

    @abc.abstractmethod
    def Validate(self, instance, value):
        """返回验证后的值"""


class Quantity(Validated):
    """value 必须大于0的属性类"""

    def Validate(self, instance, value):
        if value <= 0:
            raise ValueError("value must be > 0.")
        return value


class NonBlank(Validated):
    """value 不能为空的属性值"""

    def Validate(self, instance, value):
        value = value.strip()
        if len(value) == 0:
            raise ValueError("value cannot be empty or blank")
        return value


# 类装饰器
def Entity(cls):
    for name, attr in cls.__dict__.items():
        if isinstance(attr, Validated):
            type_name = type(attr).__name__
            attr.storage_name = "_{}#{}".format(type_name, name)
    return cls


@Entity
class LineItem:
    descript = NonBlank()  # 商品描述属性为不能为空的描述类
    weight = Quantity()  # 使用新的描述类代替
    price = Quantity()

    def __init__(self, description, weight, price):
        self.descript = description
        self.weight = weight
        self.price = price

    def Subtotal(self):
        return self.weight * self.price


raisins = LineItem('Golden raisins', 10, 6.0)

# 未使用装饰器打印：{'_NonBlank#0': 'Golden raisins', '_Quantity#0': 10, '_Quantity#1': 6.0}
# 使用装饰器后打印：{'_NonBlank#descript': 'Golden raisins', '_Quantity#weight': 10, '_Quantity#price': 6.0}
print(raisins.__dict__)

MyClass = type("MyClass", (object,), {"x": 42, "func": lambda self: self.x * 2})


class MyClass2:
    x = 42

    def func(self):
        return self.x * 2
