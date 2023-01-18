from .common import Frontpage, ImageFormat, split_notes, tomli_loads
from .const import Gallery_Toml_Path, Index_HTML


def new_gallery(title:str) -> dict:
    return dict(
        
        # 圖庫作者
        author='佚名',
        
        # 圖庫簡介 (純文本格式, 第一行是圖庫標題)
        notes=title,
        
        # 圖庫的故事 (Markdown格式)
        story='',
        
        # 圖庫首頁的展示方式
        frontpage=Frontpage.Story.name,
        
        # 相冊列表
        albums=[],
        
        # sha1, 用於判斷圖庫首頁 HTML 是否需要更新
        checksum='',
        
        # 是否使用 http proxy
        use_proxy=False,
        http_proxy='http://127.0.0.1:1081',
        
        # 圖片寬度與高度上限, 單位: 像素
        image_width_max=1000,
        image_height_max=1000,
        
        # 圖片體積上限, 單位: MB
        image_size_max=2,
        
        # 縮小圖片或生成縮略圖時, 輸出的圖片格式
        image_output_format=ImageFormat.JPEG.name,
        
        # 縮略圖邊長 (縮略圖總是正方形)
        thumb_size=128,
        
        # 以下 5 項是 Cloudflare R2 相關信息
        endpoint_url='https://<accountid>.r2.cloudflarestorage.com',
        aws_access_key_id = '<access_key_id>',
        aws_secret_access_key = '<access_key_secret>',
        bucket_name = '<bucket_name>',
        bucket_url = '<bucket_url>'
    )


def load_gallery() -> dict:
    """從硬碟中讀取 gallery.toml 的信息"""
    gallery = tomli_loads(Gallery_Toml_Path)
    gallery['notes'] = gallery['notes'].strip()
    gallery['story'] = gallery['story'].strip()
    gallery['frontpage'] = gallery['frontpage'].capitalize()
    bucket_url = gallery['bucket_url']
    gallery['bucket_url'] = bucket_url.rstrip("/") + "/"
    return gallery


def add_album(gallery:dict, album_name:str):
    gallery['albums'].insert(0, album_name)


def get_title(gallery:dict):
    """
    :return: (title, err)
    """
    title, _, err = split_notes(gallery['notes'])
    return title, err


def get_r2_html_url(gallery:dict) -> str:
    """R2 首頁的完整網址"""
    return f"{gallery['bucket_url']}{Index_HTML}"
