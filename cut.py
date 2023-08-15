import os

directory = r"D:\INS\cat"

# 遍历目录中的文件
for filename in os.listdir(directory):
    if "thumb" in filename:
        file_path = os.path.join(directory, filename)
        os.remove(file_path)