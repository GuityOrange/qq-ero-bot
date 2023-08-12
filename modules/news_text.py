from creart import create

from graia.broadcast import Broadcast
from graia.ariadne import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.model import Group
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Plain

bcc = create(Broadcast)


@bcc.receiver(GroupMessage)
async def news(app: Ariadne, group: Group, message: MessageChain):
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