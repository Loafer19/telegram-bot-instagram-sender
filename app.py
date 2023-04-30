from instagrapi import Client

cl = Client()
# cl.login('ruslan_popelyshyn', 'password', verification_code='')

media_pk = cl.media_pk_from_url("https://www.instagram.com/reels/Cqnwc6-J11V")
media_path = cl.video_download(media_pk)

print(media_path)
