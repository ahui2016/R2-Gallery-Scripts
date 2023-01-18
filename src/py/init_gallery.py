import sys

from r2g.const import CWD, Gallery_Toml_Path
from r2g.util import check_root_dir, render_gallery_toml

from r2g.gallery import new_gallery


if __name__ == "__main__":
    check_root_dir()

    if Gallery_Toml_Path.exists():
        print(f'Error: 文件已存在: {Gallery_Toml_Path}')
        sys.exit(1)

    gallery = new_gallery(CWD.name)
    render_gallery_toml(gallery)
    print('圖庫創建成功。')
    print(f'請用文本編輯器打開 {Gallery_Toml_Path} 填寫圖庫信息。')

