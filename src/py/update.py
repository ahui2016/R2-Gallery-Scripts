import r2g.gallery as Gallery
from r2g.gallery import load_gallery
from r2g.util import (
    check_initialized, render_gallery_toml, render_album_toml,
    print_err_exist
)

if __name__ == "__main__":
    check_initialized()
    
    gallery = load_gallery()
    all_albums_pics, err = Gallery.albums_pics(gallery)
    print_err_exist(err)
