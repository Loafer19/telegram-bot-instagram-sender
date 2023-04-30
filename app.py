from helpers import folder
from getpass import getpass
from instagrapi import Client
from instagrapi.exceptions import LoginRequired


def login():
    username: str = input("Username: ")
    password: str = getpass("Password: ")
    pass2fa: str = input("2FA: ")

    instagram.login(username, password, verification_code=pass2fa)


def download_media(url: str):
    media_pk: int = instagram.media_pk_from_url(url)
    return instagram.video_download(media_pk, folder=folder("videos"))


instagram = Client()

while True:
    url: str = input("URL: ")

    try:
        download_media(url)
    except LoginRequired:
        login()
        download_media(url)
    finally:
        print("Done!")
