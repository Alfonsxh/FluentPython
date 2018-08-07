"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 18-01-Flags-Asynchttp.py
@time: 18-7-30 下午10:25
@version: v1.0 
"""
import os
import time
import asyncio
import aiohttp

BASE_URL = "http://flupy.org/data/flags/"  # 基本的地址
DEST_DIR = "flags_asyncio/"  # 保存的文件夹名称

FLAGS_CC = 'CN IN US ID BR PK NG BD RU JP MX PH VN ET EG DE IR TR CD FR'.split()  # 下载的国旗缩写


def SaveFlag(img, filename):
    """
    保存国旗文件
    :param img: 原始的图片二进制数据
    :param filename: 保存的文件名称
    :return:
    """
    savePath = os.path.join(DEST_DIR, filename.lower())
    with open(savePath, "wb") as f:
        f.write(img)


def Show(flag):
    """
    显示下载
    :param flag: 国旗缩写
    :return:
    """
    print(flag, end=" ")


# 从python3.5起，开始引入了新的语法async和await
async def GetFlag(flag):
    """
    下载单面旗帜
    :param flag: 旗帜缩写名
    :return: 旗帜的数据
    """
    downloadUrl = "{base}/{flag}/{flag}.gif".format(base=BASE_URL, flag=flag.lower())
    # response = yield from aiohttp.request("GET", downloadUrl)         # 使用aiohttp.request会出现异常
    response = await aiohttp.ClientSession().get(downloadUrl)  # 将阻塞的操作交由协程完成
    image = await response.read()  # 读取响应也是异步操作
    return image


async def DownloadOne(flag):
    """
    下载单面旗帜，共异步调用
    :param flag: 旗帜的缩写名
    :return:
    """
    image = await GetFlag(flag)  # 异步获取图片的数据
    Show(flag)
    SaveFlag(image, flag + ".gif")
    return flag


def DownloadFlags(flagList: list):
    """
    下载多面旗帜
    :param flagList: 下载旗帜的列表
    :return: 下载旗帜的数量
    """
    loop = asyncio.get_event_loop()  # 返回底层的事件驱动
    toDo = [DownloadOne(cc) for cc in flagList]  # 构建单个下载的生成器队列
    waitWorker = asyncio.wait(toDo)  # 等待传进来的协程列表都结束
    complete, notComplete = loop.run_until_complete(waitWorker)  # 方法驱动，直到所有的任务都结束

    loop.close()
    return len(complete)


def main(flagsList):
    """
    主函数入口
    :param flagsList: 旗帜列表
    :return:
    """
    os.makedirs(DEST_DIR, exist_ok=True)  # 新建文件夹

    startTime = time.time()
    counts = DownloadFlags(flagsList)
    endTime = time.time()

    print("\nDownload {} flags in {}'s.".format(counts, endTime - startTime))


if __name__ == "__main__":
    main(FLAGS_CC)
