from pathlib import Path

from .const import Album_Toml
from .common import Frontpage, SortBy


def new_album(foldername:str) -> dict:
    return dict(
        
        # 作者, 留空表示等同圖庫作者
        author='',
        
        # 相冊簡介 (純文本格式, 第一行是相冊標題)
        notes=foldername,
        
        # 相冊的故事 (Markdown格式)
        story='',
        
        # 相冊內的圖片的排序方式
        sort_by=SortBy.CTimeDesc.name,
        
        # 圖片文件名列表
        pictures=[],
        
        # 封面 (一個圖片的文件名)
        cover='',
        
        # 相冊首頁的展示方式
        frontpage=Frontpage.Story.name,
        
        # sha1, 用於判斷相冊首頁 HTML 是否需要更新
        checksum='',
    )


def pics_path(album_path:Path) -> list[Path]:
    """獲取指定相冊內全部圖片的路徑"""
    pics = []
    for file in album_path.iterdir():
        if file.is_file() and file.name != Album_Toml:
            pics.append(file)
    return pics
