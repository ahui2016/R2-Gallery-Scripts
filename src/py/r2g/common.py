from enum import Enum, auto


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
