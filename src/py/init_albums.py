from pathlib import Path

import r2g.gallery as Gallery
from r2g.gallery import load_gallery
from r2g.album import new_album
from r2g.const import Albums_Path, Metadata, Thumbs, Album_Toml
from r2g.common import check_filename
from r2g.util import (
    check_initialized, render_gallery_toml, render_album_toml,
    print_err_exist
)


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


def init_album(album_path:Path, gallery:dict):
    metadata_path = album_path.joinpath(Metadata)
    thumbs_path = album_path.joinpath(Thumbs)
    thumbs_path.mkdir()
    metadata_path.mkdir()
    
    album_name = album_path.name
    album = new_album(album_name)
    album_toml_path = album_path.joinpath(Album_Toml)
    render_album_toml(album, album_toml_path)

    Gallery.add_album(gallery, album_name)
    print(f"相冊創建成功: {album_name}。")
    print(f"請用文本編輯器打開 {album_toml_path} 填寫相冊信息。")


if __name__ == "__main__":
    check_initialized()
    
    folders = get_all_albums()
    new_albums = get_new_albums(folders)
    if len(new_albums) == 0:
        print_err_exist(
            'Warning: 未發現新相冊 (注意, 新相冊必須是空文件夾)。\n'
            '請在 "albums" 文件夾內創建新文件夾後再運行 init_albums.py')

    for album in new_albums:
        if err := check_filename(album.name):
            print(f'Error: 文件夾名錯誤: {album.name}')
            print_err_exist(err)

    gallery = load_gallery()
    for album_path in new_albums:
        init_album(album_path, gallery)
    
    render_gallery_toml(gallery)
