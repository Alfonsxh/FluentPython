"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 18-03-Spinner-Asyncio.py
@time: 18-8-6 下午10:53
@version: v1.0 
"""
import asyncio
import itertools
import sys
import time


@asyncio.coroutine
def spin(msg):
    """
    打印信息
    :param msg: 附加的信息
    :return:
    """
    status = ""
    write = sys.stdout.write
    flush = sys.stdout.flush  # flush 将stdout缓存清空，内容直接打印
    for char in itertools.cycle("|/-\\"):  # itertools.cycle用于生成循环的元素
        status = char + " " + msg
        write(status)
        flush()
        write("\x08" * len(status))  # 使用 0x08 退格符将光标回退
        try:
            yield from asyncio.sleep(0.1)   # 协程中不建议使用time.sleep(...)函数代替！会阻塞事件循环！
        except asyncio.CancelledError:
            break           # 等待spin函数苏醒，如果外部取消，则会抛出CancelledError异常
    write(" " * len(status) + "\x08" * len(status))


@asyncio.coroutine
def slow_function():
    """
    思考函数
    :return: 返回思考结果
    """
    yield from asyncio.sleep(3)     # 将控制权交还给主循环
    return 43


@asyncio.coroutine
def supervisor():
    """
    事件驱动的参数函数
    :return: 返回思考结果
    """
    spinner = asyncio.async(spin("thinking"))         # update asyncio.async to asyncio.ensure_future
    # spinner = asyncio.ensure_future(spin("thinking"))
    print("Spinner -> {} begin.".format(spinner))
    result = yield from slow_function()
    spinner.cancel()
    return result


def main():
    loop = asyncio.get_event_loop()         # 获取事件循环
    result = loop.run_until_complete(supervisor())      # 驱动supervisor协程，返回参数返回的结果
    loop.close()        # 关闭事件驱动
    print("Answer:", result)


if __name__ == '__main__':
    startTime = time.time()
    main()
    print("Use Time:", time.time() - startTime)
