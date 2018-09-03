"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 19-07-Property.py
@time: 18-8-18 下午7:22
@version: v1.0
"""


# ----------------------------------------原始------------------------------------------
class LineItem:
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def SubTotal(self):
        return self.weight * self.price


raisins = LineItem('Golden raisins', 10, 6.0)
print(raisins.SubTotal())
raisins.weight = -20
print(raisins.SubTotal())


# ----------------------------------------改进一------------------------------------------
class LineItem2(LineItem):
    @property
    def weight(self):  # 必须与属性(Attribute)名称相同
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value > 0:
            self.__weight = value
        else:
            raise ValueError("value must be > 0")

    def GetPrice(self):
        return self.__price

    def SetPrice(self, value):
        if value > 0:
            self.__price = value
        else:
            raise ValueError("value must be > 0")

    price = property(GetPrice, SetPrice)


raisins2 = LineItem2('Golden raisins', 10, 6.0)
print(vars(raisins2))
print((raisins2.weight, raisins2.price))


# ----------------------------------------改进二------------------------------------------
class LineItem3(LineItem):
    def GetWeight(self):
        return self.__weight

    def SetWeight(self, value):
        if value > 0:
            self.__weight = value
        else:
            raise ValueError("value must be > 0")

    weight = property(GetWeight, SetWeight, doc="weight in kilograms")  # 构建公开的property对象，然后赋值给公开的类属性


raisins3 = LineItem3('Golden raisins', 10, 6.0)

# obj.attr这样的表达式不会从实例obj中开始寻找attr，而是从obj.__class__开始，
# 仅当类中没有名为attr的特性时，才会在实例obj中寻找attr
print(raisins3.__class__.weight)
print(raisins3.weight)
print(help(LineItem3.weight))


# ----------------------------------------改进三(工厂函数)------------------------------------------
def Quantity(storage_name):
    def QtyGetter(instance):
        return instance.__dict__[storage_name]

    def QtySetter(instance, value):
        if value > 0:
            instance.__dict__[storage_name] = value
        else:
            raise ValueError("value must be > 0")

    def QtyDeleter(instance):  # 仅实例调用
        if storage_name in instance.__dict__.keys():
            del instance.__dict__[storage_name]
        else:
            print("Del {0} fail, {0} not in.".format(storage_name))

    return property(QtyGetter, QtySetter, QtyDeleter, doc="weight in kilograms")


class LineItem4(LineItem):
    weight = Quantity("weight")
    price = Quantity("price")


raisins4 = LineItem4('Golden raisins', 10, 6.0)
print(raisins4)
print(raisins4.weight)
print(raisins4.__class__.weight)
print(LineItem4.weight)
print(raisins4.price)
print(raisins4.__class__.price)
print(LineItem4.price)
print(raisins4.__dict__)
print(raisins4.__class__.__dict__)
# del raisins4.weight
# print(raisins4.__dict__)
# print(raisins4.__class__.__dict__)
del LineItem4.weight
print(raisins4.__dict__)
print(raisins4.__class__.__dict__)

print("\n\n")
print('\ndir(raisins4) -> ', dir(raisins4))
print('\ngetattr(raisins4, "price") -> ', getattr(raisins4, "price"))
print('\nhasattr(raisins4, "price") -> ', hasattr(raisins4, "price"))
setattr(raisins4, "newattr", 10)
# print('setattr(raisins4, "newattr", 10) -> ', LineItem4.newattr)  # 类中不含此属性
print('\nsetattr(raisins4, "newattr", 10) -> ', raisins4.newattr)
print('\nvars(raisins4) -> ', vars(raisins4))
print('\nvars() -> ', vars())
