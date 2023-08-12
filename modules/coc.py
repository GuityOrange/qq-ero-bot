from creart import create
import re

from graia.broadcast import Broadcast
from graia.ariadne import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.model import Group
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Plain

bcc = create(Broadcast)


@bcc.receiver(GroupMessage)
async def coc(app: Ariadne, group: Group, message: MessageChain):
    if re.search(r'新建人物(.*)', message.display):
        if re.search(r'新建人物(.*)', message.display).group(1) == '':
            await app.send_message(
                group,
                MessageChain([Plain('请输入人物名称')]),
            )
            return

        import random
        attr_dic = {}
        name = re.search(r'新建人物(.*)', message.display).group(1).strip()
        attr_dic['名称'] = name
        attr_dic['力量'] = (random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6))*5
        attr_dic['体质'] = (random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6))*5
        attr_dic['体型'] = (random.randint(1, 6) + random.randint(1, 6) + 6)*5
        attr_dic['敏捷'] = (random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6))*5
        attr_dic['外貌'] = (random.randint(1, 6) + random.randint(1, 6) + 6)*5
        attr_dic['智力'] = (random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6))*5
        attr_dic['理智'] = (random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6))*5
        attr_dic['教育'] = (random.randint(1, 6) + random.randint(1, 6) + 6)*5
        attr_dic['幸运'] = (random.randint(1, 6) + random.randint(1, 6) + 6)*5
        attr_dic['生命'] = (attr_dic['体质'] + attr_dic['体型']) // 10
        rnt_str = ''
        for key, value in attr_dic.items():
            rnt_str += f'{key}:{value}\n'

        await app.send_message(
            group,
            MessageChain([Plain(rnt_str)]),
        )

    if message.display == 'd100':
        import random
        await app.send_message(
            group,
            MessageChain([Plain(str(random.randint(0, 100)) + '/100')]),
        )
