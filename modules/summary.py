from creart import create
from datetime import datetime
import os

from graia.broadcast import Broadcast
from graia.ariadne import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.model import Group, Member
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Plain

bcc = create(Broadcast)


@bcc.receiver(GroupMessage)
async def summary(app: Ariadne, group: Group, message: MessageChain, member: Member):
    if len(message.display) > 0:
        file_path = "./persistence/record/" + str(group.id) + "/message_record.txt"

        # 获取当前时间
        current_time = datetime.now()
        time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")
        # 确保目录存在
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)
        # 确保文件存在
        if not os.path.isfile(file_path):
            with open(file_path, "w") as file:
                pass
        # 以追加模式打开文件
        with open(file_path, "a") as file:
            # 将字符串追加到文件末尾
            file.write(f'{time_string}${str(member.id)}${member.name}${message.display}\n')



