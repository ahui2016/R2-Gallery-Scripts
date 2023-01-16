import sys

import jinja2

from .const import *


loader = jinja2.FileSystemLoader(Templates_Path)
jinja_env = jinja2.Environment(
    loader=loader, autoescape=jinja2.select_autoescape()
)


def check_root_dir():
    """檢查當前文件夾是否圖庫根目錄"""
    if not R2_Gallery_Scripts_TXT_Path.exists():
        print(f'Error: 不是圖庫根目錄: {CWD}')
        sys.exit(1)


def render_write(name:str, output:Path, data:dict):
    tmpl = jinja_env.get_template(name)
    rendered = tmpl.render(data)
    print(f"render and write {output}")
    output.write_text(rendered, encoding="utf-8")


def render_gallery_toml(gallery:dict):
    render_write(Gallery_Toml, Gallery_Toml_Path, {'gallery':gallery})
