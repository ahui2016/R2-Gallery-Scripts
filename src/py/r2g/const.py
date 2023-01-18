from pathlib import Path

# 这里主要是一些字符串的常量.
# 定义字符串常量后, 有自动补全, 也能减少 typo.

Config       = 'config'
Gallery_Toml = 'gallery.toml'
Src          = 'src'
Templates    = 'templates'
Albums       = 'albums'
Album_Toml   = 'album.toml'
Metadata     = 'metadata'
Thumbs       = 'thumbs'

R2_Gallery_Scripts_TXT = 'r2-gallery-scripts.txt'


CWD = Path.cwd().resolve()
'''已經 resolve (絕對路徑)'''


Gallery_Toml_Path = CWD.joinpath(Config, Gallery_Toml)
Templates_Path    = CWD.joinpath(Src, Templates)
Albums_Path       = CWD.joinpath(Albums)

R2_Gallery_Scripts_TXT_Path = CWD.joinpath(R2_Gallery_Scripts_TXT)

