from datetime import datetime
from creart import create
from graia.ariadne.app import Ariadne
from graia.ariadne.connection.config import (
    HttpClientConfig,
    WebsocketClientConfig,
    config,
)
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.element import Plain
from graia.broadcast import Broadcast
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Forward, ForwardNode, Image
from graia.ariadne.model import Group, Member

bcc = create(Broadcast)
app = Ariadne(
    connection=config(
        2621582133,  # 你的机器人的 qq 号
        # 574306394,  # 你的机器人的 qq 号
        "GraiaxVerifyKey",  # 填入你的 mirai-api-http 配置中的 verifyKey
        # 以下两行（不含注释）里的 host 参数的地址
        # 是你的 mirai-api-http 地址中的地址与端口
        # 他们默认为 "http://localhost:8080"
        # 如果你 mirai-api-http 的地址与端口也是 localhost:8080
        # 就可以删掉这两行，否则需要修改为 mirai-api-http 的地址与端口
        HttpClientConfig(host="http://127.0.0.1:8080"),
        WebsocketClientConfig(host="http://127.0.0.1:8080"),
    ),
)


@bcc.receiver(GroupMessage)
async def setu(app: Ariadne, group: Group, message: MessageChain, member: Member):
    if message.display == "ping":
        await app.send_message(
            group,
            MessageChain([Plain("pong")]),
        )

    if message.display == "来点壁纸":
        import os
        import random
        folder_path = r"D:\INS\wallpaper"
        file_names = os.listdir(folder_path)
        random_file_name = random.choice(file_names)
        random_file_path = os.path.join(folder_path, random_file_name)
        random_file_url = random_file_path.replace("\\", "/")
        await app.send_message(
            group,
            MessageChain([Image(path=random_file_url)]),
        )

    if message.display == "无内鬼":
        import os
        import random
        folder_path = r"D:\INS\telegram\photos"
        file_names = os.listdir(folder_path)
        random_file_name = random.choice(file_names)
        random_file_path = os.path.join(folder_path, random_file_name)
        random_file_url = random_file_path.replace("\\", "/")
        await app.send_message(
            group,
            MessageChain([Image(path=random_file_url)]),
        )

    if message.display == "今日新闻":
        import requests
        import json
        response = requests.get("http://bjb.yunwj.top/php/60miao/qq.php")
        data = json.loads(response.text)
        wb_list = data["wb"]
        inf_str = ''
        for wb in wb_list:
            inf_str += wb[0] + '\n'
        await app.send_message(
            group,
            MessageChain([Plain(inf_str)]),
        )

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
        await app.send_message(
            group,
            MessageChain([Image(path=save_path)]),
        )

    if message.display == '摸鱼':
        import os
        import requests
        import json
        save_dir = r"D:\INS\moyu"
        url = r'https://api.vvhan.com/api/moyu'
        file_name = os.path.basename(url)
        save_path = os.path.join(save_dir, file_name)
        response = requests.get(url)
        with open(save_path, 'wb') as f:
            f.write(response.content)
        await app.send_message(
            group,
            MessageChain([Image(path=save_path)]),
        )

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

    if message.display == 'd2':
        await app.send_message(
            group,
            MessageChain([Plain(str(random.randint(0, 1)))]),
        )

    if message.display == 'd100':
        await app.send_message(
            group,
            MessageChain([Plain(str(random.randint(0, 100)))]),
        )


app.launch_blocking()
