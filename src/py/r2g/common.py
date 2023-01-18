import re
from enum import Enum, auto

import tomli


Filename_Forbid_Pattern = re.compile(r"[^._0-9a-zA-Z\-]")
"""文件名/文件夾名只能使用
0-9, a-z, A-Z, _(下劃線), -(短橫線), .(點)。
"""


class Frontpage(Enum):
    """圖庫/相冊首頁的展示方式"""
    Story  = auto()  # 展示簡介, 故事與列表
    Single = auto()  # 只展示一張圖片
    List   = auto()  # 只展示列表


# 注意! 本软件暂时只能使用 JPEG, 原本打算让用户自由选择格式,
# 但后来想暂时先保持简单, 以后看情况再考虑让用户选择.
class ImageFormat(Enum):
    """縮小圖片或生成縮略圖時, 輸出的圖片格式"""
    WebP = auto()
    JPEG = auto()


class SortBy(Enum):
    """相冊內的圖片的排序方式"""
    CTime     = auto()  # 按圖片拍攝或發布日期排序
    CTimeDesc = auto()  # 按圖片拍攝或發布日期排序(倒序)
    List      = auto()  # 用列表指定順序



def sort_by_from(text:str) -> SortBy:
    n = len(text)
    if n <= len("List"):
        return SortBy.List
    elif n >= len("CTimeDesc"):
        return SortBy.CTimeDesc
    else:
        return SortBy.CTime


def check_filename(name:str):
    """
    :return: 有錯返回 err:str, 無錯返回 falsy 值。
    """
    if Filename_Forbid_Pattern.search(name) is None:
        return False

    return "文件名/文件夾名只能使用 " \
           "0-9, a-z, A-Z, _(下劃線), -(短橫線), .(點)\n" \
           "注意: 不能使用空格, 請用下劃線或短橫線代替空格。"


def tomli_loads(file) -> dict:
    """正確處理 utf-16"""
    with open(file, "rb") as f:
        text = f.read()
        try:
            text = text.decode()  # Default encoding is 'utf-8'.
        except UnicodeDecodeError:
            text = text.decode("utf-16").encode("utf-8").decode("utf-8")
        return tomli.loads(text)
