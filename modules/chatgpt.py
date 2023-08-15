from creart import create
import random

from graia.broadcast import Broadcast
from graia.ariadne import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.model import Group, Member
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Plain
from revChatGPT.V1 import Chatbot
from persistence.gpt_limit import is_under_limit

from config import access_token
bcc = create(Broadcast)
LIMIT = 50
response = ''
chat_record = []


def save_chat_record(person, sentence):
    global chat_record
    if len(chat_record) >= 10:
        chat_record.pop(0)
    chat_record.append(f'{person}: {sentence}')


def get_chat_record():
    rnt_str = ''
    global chat_record
    for i in chat_record:
        rnt_str += i + '\n'
    return rnt_str


def get_response(chatbot, prompt):
    global response
    for data in chatbot.ask(
            prompt
    ):
        response = data["message"]


@bcc.receiver(GroupMessage)
async def gpt(app: Ariadne, group: Group, message: MessageChain, member: Member):
    global response
    if len(message.display) > 3 and message.display[:3] == 'gpt':
        # 本小时次数已用完
        reachable, used_count = is_under_limit(LIMIT)
        if not reachable:
            await app.send_message(
                group,
                MessageChain([Plain(f"本小时次数已用完({used_count}/{LIMIT})")]),
            )
            return

        # 本小时次数未用完,走正常流程
        chatbot = Chatbot(config={
            "access_token": access_token
        })
        prompt = '你现在是一个群聊助手，你的职责是回答问题，若问题需要你详细说明，你则按照正常回答长度回答，否则你的回答要尽量简短。并且需要在每句话之后带上”喵~“，你需要回答的问题是：'
        prompt += message.display[3:]

        response = ""
        get_response(chatbot, prompt)

        await app.send_message(
            group,
            MessageChain([Plain(response + f'({used_count}/{LIMIT})')]),
        )

    # 模拟群友随机回复，1/20概率，只有在可用条数大于一半时才会回复
    if len(message.display) > 0 and random.randint(1, 20) == 1:
        # 本小时次数已用完
        reachable, used_count = is_under_limit(LIMIT)
        if not reachable or used_count > LIMIT // 2:
            return

        # 本小时次数未用完,走正常流程
        chatbot = Chatbot(config={
            "access_token": access_token
        })
        prompt = '你现在是一个群聊成员，你需要根据群友说的话来回应，回应需要简短，而且不能有标点符号，若你不清楚群友说的话的意义，可以回答类似“确实”，“是这样的”等摸棱两可的回应。群友的对话为：' + message.display
        response = ""
        get_response(chatbot, prompt)

        await app.send_message(
            group,
            MessageChain([Plain(response)]),
        )
