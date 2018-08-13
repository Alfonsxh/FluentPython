"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 18-05-Flags-Asynchttp2.py
@time: 18-8-9 下午10:24
@version: v1.0 
"""
import os
import time
import asyncio
import aiohttp
import tqdm
import collections
from aiohttp import web

BASE_URL = "http://flupy.org/data/flags/"  # 基本的地址
DEST_DIR = "flags_asyncio2/"  # 保存的文件夹名称

FLAGS_CC = 'CN IN US ID BR PK NG BD RU JP MX PH VN ET EG DE IR TR CD FR'.split()  # 下载的国旗缩写


class FetchError(Exception):
    def __init__(self, country_code):
        self.country_code = country_code


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
    if response.status == 200:
        image = await response.read()  # 读取响应也是异步操作
        return image
    elif response.status == 404:
        raise web.HTTPNotFound
    else:
        raise aiohttp.HttpProcessingError(
            code=response.status, message=response.reason,
            headers=response.headers)


async def DownloadOne(flag, semphore, verbose):
    """
    下载单面旗帜，共异步调用
    :param flag: 旗帜的缩写名
    :param semphore:
    :param verbose:
    :return:
    """
    try:
        with await semphore:
            image = await GetFlag(flag)
    except web.HTTPNotFound:
        status = "NOT FOUND"
    except Exception as exc:
        raise FetchError(exc)
    else:
        # loop = asyncio.get_event_loop()
        # loop.run_in_executor(None, SaveFlag, image, flag + ".gif")
        SaveFlag(image, flag + ".gif")
        status = "OK"

    if verbose and status:
        print(flag, status)

    return status


async def DownloadCoro(flagList, verbose, concurReq):
    counter = collections.Counter()
    semaphore = asyncio.Semaphore(concurReq)
    to_do = [DownloadOne(flag, semaphore, verbose) for flag in sorted(flagList)]

    to_do_iter = asyncio.as_completed(to_do)

    if not verbose:
        to_do_iter = tqdm.tqdm(to_do_iter, total=len(flagList))
    for future in to_do_iter:
        try:
            result = await future
        except FetchError as exc:
            countryCode = exc.country_code
            try:
                errorMsg = exc.__cause__.args[0]
            except IndexError:
                errorMsg = exc.__cause__.__class__.__name__
            if verbose and errorMsg:
                print("***Error for {}: [}".format(countryCode, errorMsg))
        else:
            status = result

        counter[status] += 1

    return counter


def DownloadFlags(flagList: list, verbose, concurReq):
    """
    下载多面旗帜
    :param flagList: 下载旗帜的列表
    :param verbose:
    :param concurReq:
    :return: 下载旗帜的数量
    """
    loop = asyncio.get_event_loop()  # 返回底层的事件驱动
    coro = DownloadCoro(flagList, verbose, concurReq)
    counts = loop.run_until_complete(coro)
    loop.close()
    return counts


def main(flagsList):
    """
    主函数入口
    :param flagsList: 旗帜列表
    :return:
    """
    os.makedirs(DEST_DIR, exist_ok=True)  # 新建文件夹

    startTime = time.time()
    counts = DownloadFlags(flagsList, True, 100)
    endTime = time.time()

    print("\nDownload {} flags in {}'s.".format(counts, endTime - startTime))


if __name__ == "__main__":
    main(FLAGS_CC)
