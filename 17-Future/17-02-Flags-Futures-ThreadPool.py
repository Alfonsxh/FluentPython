"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 17-02-Flags-Futures-ThreadPool.py
@time: 18-7-29 下午2:28
@version: v1.0 
"""
# 下载多面旗帜，线程池方式
import os
import time
import requests
from string import ascii_lowercase
from concurrent import futures

BASE_URL = "http://flupy.org/data/flags/"
DEST_DIR = "flags_futures_thread/"

FLAGS_CC = 'CN IN US ID BR PK NG BD RU JP MX PH VN ET EG DE IR TR CD FR'.split()

MAX_WORLERS = 4


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


def GetFlag(flag):
    """
    下载单面旗帜
    :param flag: 旗帜缩写名
    :return: 旗帜的数据
    """
    downloadUrl = "{base}/{flag}/{flag}.gif".format(base=BASE_URL, flag=flag.lower())
    ret = requests.get(downloadUrl)
    if ret.status_code != 200:
        ret.raise_for_status()
    content = ret.content
    return content


def DownloadOne(flag):
    """
    下载单面旗帜，供线程使用
    :param flag: 旗帜缩写名
    :return: 旗帜的数据
    """
    try:
        image = GetFlag(flag)
    except:
        return ""
    Show(flag)
    SaveFlag(image, flag.lower() + ".gif")
    return flag


def DownloadFlags(flagList: list):
    """
    下载多面旗帜，线程池方式
    :param flagList: 下载旗帜的列表
    :return: 下载旗帜的数量
    """
    workers = min(MAX_WORLERS, len(flagList))
    with futures.ThreadPoolExecutor(workers) as exector:
        res = exector.map(DownloadOne, sorted(flagList))  # 使用线程池来下载
    return len(set(res)) - 1


def main(flagsList):
    """
    主函数入口
    :param flagsList: 旗帜列表
    :return:
    """
    os.makedirs(DEST_DIR, exist_ok=True)

    startTime = time.time()
    counts = DownloadFlags(flagsList)
    endTime = time.time()

    print("\nDownload {} flags in {}'s.".format(counts, endTime - startTime))


if __name__ == "__main__":
    # flags = [m + n for m in ascii_lowercase for n in ascii_lowercase]
    main(FLAGS_CC)
