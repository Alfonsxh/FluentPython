"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 20-01-LineItem1.py
@time: 18-8-25 下午2:35
@version: v1.0
"""


# --------------------------------------例一------------------------------------------------
class Quantity:
    def __init__(self, storage_name):
        self.storage_name = storage_name

    def __set__(self, instance, value):  # 描述符类设置属性的值，instance是托管实例
        """
        设置描述符的属性的值
        :param instance: 托管类的实例
        :param value: 需要设置的值
        :return:
        """
        if value > 0:
            instance.__dict__[self.storage_name] = value  # 在托管实例的字典表中添加对应的属性值
        else:
            raise ValueError("value must be > 0.")


class LineItem:
    weight = Quantity("weight")
    price = Quantity("price")

    def __init__(self, description, weight, price):
        self.descript = description
        self.weight = weight
        self.price = price

    def Subtotal(self):
        return self.weight * self.price


raisins = LineItem('Golden raisins', 10, 6.0)
print("raisins.__dict__ -> ", raisins.__dict__)


# --------------------------------------例二------------------------------------------------
class Quantity2:
    __counter = 0

    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__  # 类名Quantity2
        index = cls.__counter  # 使用计数代替存储的名称
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
        if value > 0:
            setattr(instance, self.storage_name, value)  # 在托管实例的字典表中添加对应的属性值
        else:
            raise ValueError("value must be > 0.")


class LineItem2:
    weight = Quantity2()
    price = Quantity2()

    def __init__(self, description, weight, price):
        self.descript = description
        self.weight = weight
        self.price = price

    def Subtotal(self):
        return self.weight * self.price


raisins2 = LineItem2('Golden raisins', 10, 6.0)
print("raisins2.__dict__ -> ", raisins2.__dict__)  # __dict__中包含的key值为_Quantity2#index
print("\n(raisins2.weight, raisins2.price) -> ", (raisins2.weight, raisins2.price))
print('(getattr(raisins2, "_Quantity2#0"), getattr(raisins2, "_Quantity2#1")) -> ',
      (getattr(raisins2, "_Quantity2#0"), getattr(raisins2, "_Quantity2#1")))

print("\n\n")


# --------------------------------------例三------------------------------------------------
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


class Quantity3(Validated):
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


class LineItem3:
    descript = NonBlank()  # 商品描述属性为不能为空的描述类
    weight = Quantity3()  # 使用新的描述类代替
    price = Quantity3()

    def __init__(self, description, weight, price):
        self.descript = description
        self.weight = weight
        self.price = price

    def Subtotal(self):
        return self.weight * self.price


try:
    raisins3 = LineItem3('', 10, 6.0)
except ValueError as e:
    print(e)

raisins3 = LineItem3('Golden raisins', 10, 6.0)
print("(raisins3.descript, raisins3.weight, raisins3.price) -> ", (raisins3.descript, raisins3.weight, raisins3.price))
print("raisins3.__dict__ -> ", raisins3.__dict__)
