import r2g.gallery as Gallery
from r2g.gallery import load_gallery, get_r2_html_url
from r2g.util import check_initialized


Version = '0.0.1'


def show_info():
    gallery = load_gallery()
    title, err = Gallery.get_title(gallery)
    if err:
        title = err

    print()
    print(f"[repo]    https://github.com/ahui2016/R2-Gallery-Scripts")
    print(f"[version] {Version}")
    print()
    print(f"[Gallery] {title}")
    print(f"[Author]  {gallery['author']}")
    print(f"[Albums]  {len(gallery['albums'])}")
    print()
    print("[R2 Home Page]")
    print(get_r2_html_url(gallery))
    print()
    print(f"[Image Width Max    ] {gallery['image_width_max']} px")
    print(f"[Image Height Max   ] {gallery['image_height_max']} px")
    print(f"[Image Size Max     ] {gallery['image_size_max']} MB")
    print(f"[Image Output Format] {gallery['image_output_format']}")
    print(f"[Thumbnail Size     ] {gallery['thumb_size']}")
    print()
    use_proxy = gallery['use_proxy']
    print(f"[use proxy] {use_proxy}")
    proxy = gallery['http_proxy']
    if not proxy and use_proxy:
        proxy = f"\n未設置 proxy"
    print(f"[http proxy] {proxy}")
    print()


if __name__ == "__main__":
    check_initialized()
    show_info()
