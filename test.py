file_path = r'D:\INS\nsfw-pic\_gCmk_-.jpg'

import cv2
# 读取图片文件
img = cv2.imread(file_path)
# 倒转图片
img_flip = cv2.flip(img, 0)
# 保存倒转后的图片
cv2.imwrite(file_path, img_flip)