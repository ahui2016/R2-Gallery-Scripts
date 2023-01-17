import sys
from pathlib import Path

from r2g.const import CWD, Albums_Path
from r2g.util import check_root_dir


def get_all_albums() -> list[Path]:
    """獲取 albums 文件夾內全部子文件夾的路徑"""
    albums = []
    for item in Albums_Path.iterdir():
        if item.is_dir():
            albums.append(item)
    return albums


def get_new_albums(albums:list[Path]) -> list[Path]:
    """空文件夾就是新相冊"""
    new_albums = []
    for album in albums:
        if count_children_of_folder(album) == 0:
            new_albums.append(album)
    return new_albums


def count_children_of_folder(folder:Path) -> int:
    n = 0
    for _ in folder.iterdir():
        n += 1
    return n


if __name__ == "__main__":
    check_root_dir()
    
    folders = get_all_albums()
    new_albums = get_new_albums(folders)
    if len(new_albums) == 0:
        print('Warning: 未發現新相冊 (注意, 新相冊必須是空文件夾)。/n' \
              '請在 "albums" 文件夾內創建新文件夾後再運行 init_albums.py')
