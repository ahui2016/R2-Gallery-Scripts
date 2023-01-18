import re
from enum import Enum, auto

import tomli


Filename_Forbid_Pattern = re.compile(r"[^._0-9a-zA-Z\-]")
"""文件名/文件夾名只能使用
0-9, a-z, A-Z, _(下劃線), -(短橫線), .(點)。
"""

Short_Notes_Limit = 512
"""簡單描述(notes)的長度上限, 單位: UTF8字符"""

Title_Limit = 32
"""標題的長度上限, 單位: UTF8字符"""


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


def split_notes(text:str):
    """
    :return: (標題, 簡介, 錯誤)
    """
    title, notes = split_first_line(text)
    err = None
    if not title:
        err = "未填寫notes"
    return title, notes, err


def split_first_line(text:str):
    """將 text 分成兩部分, 第一行是第一部分, 其餘是第二部分.
    其中第一行長度限制.

    注意, 有可能返回空字符串.
    """
    text = text.strip()
    parts = text.split("\n", maxsplit=1)
    if len(parts) < 2:
        parts.append("")
    head, tail = parts[0].strip(), parts[1].strip()
    if len(head) > Title_Limit:
        head = head[:Title_Limit]
    return head, tail
