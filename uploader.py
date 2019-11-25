import os
import time
from pathlib import Path
from telethon import TelegramClient
from telethon.tl.functions.channels import CreateChannelRequest, EditPhotoRequest
from telethon.tl.types import InputChatUploadedPhoto

# TODO Put your API id and API hash. You can get new ones here https://my.telegram.org/apps
api_id = 4815162342
api_hash = 'hash'
client = TelegramClient('session_name', api_id, api_hash)

# TODO Enter your channel name prefix (for fast search) and the path of albums
prefix = "recpl"
path = r"/media/recvec/DE3C1FD03C1FA317/The Left Banke"


async def channel_init(prefix, folder):
    channel_name = prefix + " - " + folder.split(os.sep)[-2] + " - " + folder.split(os.sep)[-1]
    print("channel name: " + channel_name)
    createdPrivateChannel = await client(CreateChannelRequest(channel_name, "", megagroup=False))
    newChannelID = createdPrivateChannel.__dict__["chats"][0].__dict__["id"]
    print("new channel ID " + str(newChannelID))
    return newChannelID


async def icon_init(folder, newChannelID):
    icon = list(Path(folder + "/").glob("*.jpg"))[0]
    channel_entity = await client.get_entity(newChannelID)
    upload_file_result = await client.upload_file(file=str(icon))
    input_chat_uploaded_photo = InputChatUploadedPhoto(upload_file_result)
    return channel_entity, input_chat_uploaded_photo


async def upload_icon(channel_entity, input_chat_uploaded_photo):
    try:
        result = await client(EditPhotoRequest(channel=channel_entity,
                                               photo=input_chat_uploaded_photo))
        print("successfully uploaded icon")
    except BaseException as e:
        print(e)
        sec = [int(s) for s in e.split() if s.isdigit()][0] + 5
        print(str(sec) + " seconds to sleep 💋💋💋💋💋💋💋💋")

        time.sleep(sec)
        print("stop sleeping 💋💋💋💋💋💋💋")
        await upload_icon(channel_entity, input_chat_uploaded_photo)


async def upload_songs(folder, newChannelID):
    for f in sorted(Path(folder + "/").glob("*.mp3")):
        print("uploading song:" + str(f))
        await client.send_file(newChannelID, f)
        print("successfully uploaded song")


async def main():
    folders = list(map((lambda x: os.path.join(path, x)), os.listdir(path)))

    await client.start()

    for folder in folders:
        new_channel_id = await channel_init(prefix, folder)
        await upload_songs(folder, new_channel_id)

        channel_entity, input_chat_uploaded_photo = await icon_init(folder, new_channel_id)
        await upload_icon(channel_entity, input_chat_uploaded_photo)


with client:
    client.loop.run_until_complete(main())
