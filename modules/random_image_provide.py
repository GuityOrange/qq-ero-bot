from creart import create
import asyncio

from graia.broadcast import Broadcast
from graia.ariadne import Ariadne
from graia.ariadne.event.message import GroupMessage, MessageEvent
from graia.ariadne.model import Group
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Plain
from graia.ariadne.message.element import Image

bcc = create(Broadcast)


@bcc.receiver(GroupMessage)
async def setu(app: Ariadne, group: Group, message: MessageChain, event: MessageEvent):
    if message.display == "来点壁纸":
        import os
        import random
        folder_path = r"D:\INS\wallpaper"
        file_names = os.listdir(folder_path)
        random_file_name = random.choice(file_names)
        random_file_path = os.path.join(folder_path, random_file_name)
        random_file_url = random_file_path.replace("\\", "/")
        bot_message = await app.send_message(
            group,
            MessageChain([Image(path=random_file_url)]),
        )
        await asyncio.sleep(60)
        await app.recall_message(bot_message)
        await app.recall_message(event.source)

    if message.display == "插画":
        import os
        import random
        folder_path = r"D:\INS\pixiv"
        file_names = os.listdir(folder_path)
        random_file_name = random.choice(file_names)
        random_file_path = os.path.join(folder_path, random_file_name)
        random_file_url = random_file_path.replace("\\", "/")
        bot_message = await app.send_message(
            group,
            MessageChain([Image(path=random_file_url)]),
        )
        # await asyncio.sleep(60)
        # await app.recall_message(bot_message)
        # await app.recall_message(event.source)

    if message.display == "无内鬼":
        import os
        import random
        folder_path = r"D:\INS\telegram\photos"
        file_names = os.listdir(folder_path)
        random_file_name = random.choice(file_names)
        random_file_path = os.path.join(folder_path, random_file_name)
        random_file_url = random_file_path.replace("\\", "/")
        bot_message = await app.send_message(
            group,
            MessageChain([Image(path=random_file_url)]),
        )
        # await asyncio.sleep(60)
        # await app.recall_message(bot_message)
        # await app.recall_message(event.source)

    if message.display == "猫猫":
        import os
        import random
        folder_path = r"D:\INS\cat"
        file_names = os.listdir(folder_path)
        random_file_name = random.choice(file_names)
        random_file_path = os.path.join(folder_path, random_file_name)
        random_file_url = random_file_path.replace("\\", "/")
        bot_message = await app.send_message(
            group,
            MessageChain([Image(path=random_file_url)]),
        )
        # await asyncio.sleep(60)
        # await app.recall_message(bot_message)
        # await app.recall_message(event.source)

    if message.display == 'sfw':
        import os
        import requests
        import json
        response = requests.get("https://api.waifu.pics/sfw/waifu")
        save_dir = r"D:\INS\pic"
        data = json.loads(response.text)
        url = data["url"]
        file_name = os.path.basename(url)
        save_path = os.path.join(save_dir, file_name)
        response = requests.get(url)
        with open(save_path, 'wb') as f:
            f.write(response.content)
        bot_message = await app.send_message(
            group,
            MessageChain([Image(path=save_path)]),
        )
        await asyncio.sleep(60)
        await app.recall_message(bot_message)
        await app.recall_message(event.source)

    if message.display == 'nsfw':
        import os
        import requests
        import json
        response = requests.get("https://api.waifu.pics/nsfw/waifu")
        data = json.loads(response.text)
        url = data["url"]
        await app.send_message(
            group,
            MessageChain(url),
        )
