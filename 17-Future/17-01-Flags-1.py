"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 17-01-Flags-1.py
@time: 18-7-29 下午2:28
@version: v1.0 
"""
# 国旗下载程序，依序下载
import os
import time
import requests

BASE_URL = "http://flupy.org/data/flags/"  # 基本的地址
DEST_DIR = "flags/"  # 保存的文件夹名称

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


def DownloadOne(flag):
    """
    下载单面旗帜
    :param flag: 旗帜缩写名
    :return: 旗帜的数据
    """
    downloadUrl = "{base}/{flag}/{flag}.gif".format(base=BASE_URL, flag=flag.lower())
    ret = requests.get(downloadUrl)
    content = ret.content
    return content


def DownloadFlags(flagList: list):
    """
    下载多面旗帜
    :param flagList: 下载旗帜的列表
    :return: 下载旗帜的数量
    """
    for flag in sorted(flagList):
        image = DownloadOne(flag)
        Show(flag)
        SaveFlag(image, flag.lower() + ".gif")
    return len(flagList)


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
