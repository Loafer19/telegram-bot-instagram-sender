from helpers import folder
from getpass import getpass
from instagrapi import Client
from instagrapi.exceptions import LoginRequired

instagram = Client()


def login():
    username: str = input("Username: ")
    password: str = getpass("Password: ")
    pass2fa: str = input("2FA: ")

    instagram.login(username, password, verification_code=pass2fa)


def download_media(url: str):
    try:
        media_pk: int = instagram.media_pk_from_url(url)
        return instagram.video_download(media_pk, folder=folder("videos"))
    except LoginRequired:
        login()
        download_media(url)
