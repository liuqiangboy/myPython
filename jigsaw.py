# -*- coding:utf-8 -*-
import os
from PIL import Image
from math import sqrt,ceil
from time import asctime

# import pyautogui
# import re

def jigsaw(width_i=200,height_i=200,dir_path='keyFrames/'):
# width_i*height_i,图片压缩后的大小
    # 参数初始化
    all_path = []
    num = 0


    dirName = dir_path

    for root, dirs, files in os.walk(dirName):
        for file in files:
            if "jpeg"  in file or 'jpg' in file:
                all_path.append(os.path.join(root, file))

    all_path=sorted(all_path)

    image_numbers=len(all_path)
    if image_numbers==0:
        return
    line_max=int(ceil(sqrt(image_numbers)))
    row_max=line_max
    pic_max = line_max * row_max
    toImage = Image.new('RGBA', (width_i * line_max, height_i * row_max))
    # 转换为的图片的总大小
    for i in range(0, row_max):
        for j in range(0, line_max):
            if num >= image_numbers:
                print("break")
                break
            pic_fole_head = Image.open(all_path[num])
            width, height = pic_fole_head.size

            tmppic = pic_fole_head.resize((width_i, height_i))

            loc = (int(j % line_max * width_i), int(i % line_max * height_i))

            # print("第" + str(num) + "存放位置" + str(loc))
            toImage.paste(tmppic, loc)
            num = num + 1

        if num >= pic_max:
            break

    print(toImage.size)
    toImage.save('res/'+asctime()+'.png')
if __name__=='__main__':
    jigsaw()
