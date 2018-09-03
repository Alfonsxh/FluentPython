"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 21-03-Import-And-Runtime.py
@time: 18-9-3 下午10:47
@version: v1.0 
"""

print("<[1]> Import and runtime moudle start")


class ClassOne:
    print("<[2]> ClassOne body")

    def __init__(self):
        print("<[3]> ClassOne.__init__")

    def __del__(self):
        print("<[4] ClassOne.__del__>")

    def MethodX(self):
        print("<[5] ClassOne.MethodX>")

    class ClassTwo:
        print("<[6]> ClassTwo body")


import evalsupport


@evalsupport.ClsDecorator
class ClassThree:
    print("<[7]> ClassThree body")

    def MethodY(self):
        print("<[8] ClassThree.MethodY>")


class ClassFour(ClassThree):
    print("<[9]> ClassFour body")

    def MethodY(self):
        print("<[10] ClassFour.MethodY>")


class ClassFive(metaclass=evalsupport.MetaAleph):
    print("<[11]> ClassFive body")

    def __init__(self):
        print("<[12]> ClassFive.__init__")

    def MethonZ(self):
        print("<[13]> ClassFive.MethonZ")


class ClassSix(ClassFive):
    print("<[14] ClassSix body>")

    def MethonZ(self):
        print("<[15] ClassSix.MethonZ>")


if __name__ == "__main__":
    print("<[16]> ClassOne tests", 30 * "*")
    one = ClassOne()
    one.MethodX()

    print("<[17]> ClassThree tests", 30 * "*")
    three = ClassThree()
    three.MethodY()

    print("<[18]> ClassFour tests", 30 * "*")
    four = ClassFour()
    four.MethodY()

    print("<[19]> ClassFive tests", 30 * "*")
    five = ClassFive()
    five.MethodZ()

    print("<[20]> ClassFive tests", 30 * "*")
    six = ClassSix()
    six.MethodZ()

print("<[21]> Import and runtime moudle end")
