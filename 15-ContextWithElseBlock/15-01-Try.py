"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 15-01-Try.py
@time: 18-7-1 下午10:42
@version: v1.0 
"""

try:
    print("I'm try.")
except:
    print("I'm except.")        # 如果在异常处理中出现异常，finally仍然执行！
else:
    print("I'm else.")          # 未抛出异常时执行
finally:
    print("I'm finally.")       # 不管与否都执行！！！
