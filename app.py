from instagram import download_media

while True:
    url: str = input("URL: ")

    download_media(url)

    print("Downloaded!")
