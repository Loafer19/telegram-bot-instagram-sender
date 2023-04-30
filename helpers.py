from os import path, makedirs


def create_folder(folder_name: str) -> str:
    makedirs(folder_name, exist_ok=True)

    return path.realpath(folder_name)


def folder(folder_name: str, ensure: bool = True) -> str:
    if ensure:
        return create_folder(folder_name)

    return path.realpath(folder_name)
