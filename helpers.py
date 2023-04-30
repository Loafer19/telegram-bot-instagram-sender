from os import path, makedirs


def folder(name: str) -> str:
    makedirs(name, exist_ok=True)

    return path.realpath(name)
