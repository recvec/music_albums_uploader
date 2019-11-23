import os
import re
import time
from locale import atoi
from pathlib import Path

from telethon import TelegramClient
from telethon.tl.functions.channels import CreateChannelRequest, EditPhotoRequest
from telethon.tl.types import InputChatUploadedPhoto

api_id = "id"
api_hash = 'hash'
client = TelegramClient('session_name', api_id, api_hash)


async def upload_icon(channel_entity, input_chat_uploaded_photo):
    try:
        result = await client(EditPhotoRequest(channel=channel_entity,
                                               photo=input_chat_uploaded_photo))
    except BaseException as e:
        print(e)
        sec = [int(s) for s in e.split() if s.isdigit()][0] + 5
        print(str(sec) + " seconds to sleep 💋💋💋💋💋💋💋💋")

        time.sleep(sec)
        print("stop sleeping 💋💋💋💋💋💋💋")
        await upload_icon(channel_entity, input_chat_uploaded_photo)


async def main():
    prefix = "recpl"
    path = r"/media/recvec/D/Artist"
    folders = list(map((lambda x: os.path.join(path, x)), os.listdir(path)))

    await client.start()

    for folder in folders:

        channel_name = prefix + " - " + folder.split("/")[-2] + " - " + folder.split("/")[-1]
        print(channel_name)
        createdPrivateChannel = await client(CreateChannelRequest(channel_name, "", megagroup=False))
        newChannelID = createdPrivateChannel.__dict__["chats"][0].__dict__["id"]
        print(newChannelID)
        print(folder)

        icon = list(Path(folder + "/").glob("*.jpg"))[0]
        channel_entity = await client.get_entity(newChannelID)
        upload_file_result = await client.upload_file(file=str(icon))
        input_chat_uploaded_photo = InputChatUploadedPhoto(upload_file_result)
        await upload_icon(channel_entity, input_chat_uploaded_photo)

        print('finish')
        for f in sorted(Path(folder + "/").glob("*.mp3")):
            print(f)
            await client.send_file(newChannelID, f)


with client:
    client.loop.run_until_complete(main())


def natural_keys(text):
    return [atoi(c) for c in re.split(r'(\d+)', text)]
