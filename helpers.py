from os import path, makedirs


def folder(name: str) -> str:
    makedirs(name, exist_ok=True)

    return path.realpath(name)


def is_instagram_url(url: str) -> str:
    return "instagram.com/reel" in url


def format_caption_from_url(url: str) -> str:
    return "Downloaded from [Instagram](%s) by @Loafer19" % url
