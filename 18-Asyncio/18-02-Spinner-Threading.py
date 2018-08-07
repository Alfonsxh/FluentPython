"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 18-02-Spinner-Threading.py
@time: 18-8-6 下午10:52
@version: v1.0 
"""
import threading
import time
import itertools
import sys


class Signal:
    go = True


def spin(msg, signal):
    """
    打印过程
    :param msg: 特殊消息
    :param signal: 线程停止信号
    :return:
    """
    status = ""
    write = sys.stdout.write
    flush = sys.stdout.flush    # flush 将stdout缓存清空，内容直接打印
    for char in itertools.cycle("|/-\\"):  # itertools.cycle用于生成循环的元素
        status = char + " " + msg
        write(status)
        flush()
        write("\x08" * len(status))  # 使用 0x08 退格符将光标回退
        time.sleep(0.1)
        if not signal.go:  # 线程退出标识
            break
    write(" " * len(status) + "\x08" * len(status))


def slow_function():
    """
    模拟思考过程
    :return: 结果
    """
    time.sleep(3)
    return 43


def supervisor():
    """
    启动线程开始执行
    :return: 返回结果
    """
    signal = Signal()
    spinner = threading.Thread(target=spin, args=("thinking", signal))
    print("Spinner object -> {} begin".format(spinner))
    spinner.start()
    result = slow_function()
    signal.go = False
    spinner.join()
    return result


def main():
    result = supervisor()
    print("Answer:", result)


if __name__ == "__main__":
    startTime = time.time()
    main()
    print("Use Time:", time.time() - startTime)
