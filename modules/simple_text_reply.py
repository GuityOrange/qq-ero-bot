from creart import create

from graia.broadcast import Broadcast
from graia.ariadne import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.model import Group
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Plain

bcc = create(Broadcast)


@bcc.receiver(GroupMessage)
async def setu(app: Ariadne, group: Group, message: MessageChain):
    if message.display == "ping":
        await app.send_message(
            group,
            MessageChain([Plain("pong")]),
        )

    if message.display == '回答':
        import random
        rnt = '是' if random.randint(1, 2) == 1 else '否'
        await app.send_message(
            group,
            MessageChain([Plain(rnt)]),
        )

    if message.display == 'd100':
        import random
        await app.send_message(
            group,
            MessageChain([Plain(str(random.randint(0, 100)) + '/100')]),
        )
