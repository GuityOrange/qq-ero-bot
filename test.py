# https://api.waifu.pics/nsfw/waifu
import os
import requests
import json
response = requests.get("https://api.waifu.pics/sfw/waifu")
save_dir = r"D:\INS\pic"
data = json.loads(response.text)
url = data["url"]
print('url', url)

# 从URL中解析出图片文件名
file_name = os.path.basename(url)
# 拼接保存图片的完整路径
save_path = os.path.join(save_dir, file_name)
# 发送HTTP请求并保存图片到本地
response = requests.get(url)
with open(save_path, 'wb') as f:
    f.write(response.content)
print(save_path)