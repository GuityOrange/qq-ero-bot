from creart import create
import re

from graia.broadcast import Broadcast
from graia.ariadne import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.model import Group
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Plain
from revChatGPT.V1 import Chatbot
from persistence.gpt_limit import is_under_limit

bcc = create(Broadcast)
LIMIT = 50
response = ''


def get_response(chatbot, prompt):
    global response
    for data in chatbot.ask(
            prompt
    ):
        response = data["message"]


@bcc.receiver(GroupMessage)
async def gpt(app: Ariadne, group: Group, message: MessageChain):
    if re.search(r'gpt(.*)', message.display):
        # 输入内容为空
        if re.search(r'gpt(.*)', message.display).group(1) == '':
            await app.send_message(
                group,
                MessageChain([Plain('请输入你想问gpt的内容')]),
            )
            return

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
            "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiI1NzQzMDYzOTRAcXEuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWV9LCJodHRwczovL2FwaS5vcGVuYWkuY29tL2F1dGgiOnsidXNlcl9pZCI6InVzZXItMkVTazRWUEhCa213c3hSWWRMejU5TE9PIn0sImlzcyI6Imh0dHBzOi8vYXV0aDAub3BlbmFpLmNvbS8iLCJzdWIiOiJhdXRoMHw2MzhlMGJjNGRhYTJjMzQwMGViNzI2NWQiLCJhdWQiOlsiaHR0cHM6Ly9hcGkub3BlbmFpLmNvbS92MSIsImh0dHBzOi8vb3BlbmFpLm9wZW5haS5hdXRoMGFwcC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjkxODA3OTAxLCJleHAiOjE2OTMwMTc1MDEsImF6cCI6IlRkSkljYmUxNldvVEh0Tjk1bnl5d2g1RTR5T282SXRHIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCBtb2RlbC5yZWFkIG1vZGVsLnJlcXVlc3Qgb3JnYW5pemF0aW9uLnJlYWQgb3JnYW5pemF0aW9uLndyaXRlIG9mZmxpbmVfYWNjZXNzIn0.i1EnkatW-Ca78wKnSPdfMD29au4O4dz1adDRUNQmK3ghFOGprhOJIknWorNBKgDF1RdDWpLTKpkViIZdoGbrQkZNoKB7vi3BpnS76Pye1O3vP6hYJekPvKJkI67ZXEyUV2SAc09EUoPmZZIDdQWwIfun8dbjWQ5MPJJWFJVEcfWvkyCy330OSl9KRHvFqsJAGJgs_IK2Xm3DcfZV_a-V8T1YOoQ1ZkBi9X8N7lKfJs8PeYaWW88XM3psD41WwQvW4jvTan4fgRllWXBGFzwmLTpxlHxWWzLXObdYDiRwhAvqC5MPuF-y4mI7rgqh-y-aalO5l-DW0lV8MZkgzBFYUQ"
        })
        prompt = re.search(r'(gpt.*)', message.display).group(1).strip()
        global response
        response = ""
        get_response(chatbot, prompt)

        await app.send_message(
            group,
            MessageChain([Plain(response + f'\n\n本小时使用次数({used_count}/{LIMIT})')]),
        )
