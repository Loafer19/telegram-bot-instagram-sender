from helpers import is_instagram_url, format_caption_from_url
from instagram import download_media
from pyrogram import Client, filters

telegram = Client("my_account")


@telegram.on_message(filters.text & filters.private & filters.me)
async def on_message(client, message):
    if is_instagram_url(message.text):
        file_path: str = download_media(message.text)
        caption: str = format_caption_from_url(message.text)
        await client.send_video(message.chat.id, file_path, caption)
        await message.delete()


telegram.run()
