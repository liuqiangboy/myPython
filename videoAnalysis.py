# -*- coding:utf-8 -*-
import numpy as np
import cv2
import os
from jigsaw import jigsaw
import matplotlib.pyplot as plt
import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)
import uuid
def del_file(path):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.remove(c_path)
def diff_image_sub(src_1,src_2):
    src_1 = src_1.astype(np.int)
    src_2 = src_2.astype(np.int)
    diff = abs(src_1 - src_2)
    return np.sum(diff.astype(np.uint8))
def convertImage(src):
    return cv2.cvtColor(src,cv2.COLOR_RGB2GRAY)
def diff_image_histogram(src_1,src_2):

    src_1 = convertImage(src_1)

    # plt.imshow(src_1)
    # plt.show()
    src_2 = convertImage(src_2)
    src_1 = src_1.astype(np.int)
    src_2 = src_2.astype(np.int)
    diff = abs(src_1 - src_2)
    res=np.sum(diff.astype(np.uint8))
    return res
def plt_brokenLine(x,y):
    plt.plot(x, y)
    plt.show()
fileList=['/Users/liuqiang/Downloads/视频镜头分割及关键帧提取技术的研究与实现416/猎场片花.mp4',
          '/Users/liuqiang/Downloads/视频镜头分割及关键帧提取技术的研究与实现416/表演.mp4',
          '/Users/liuqiang/Downloads/视频镜头分割及关键帧提取技术的研究与实现416/动漫.mp4',
          '/Users/liuqiang/Desktop/镜头分割/功守道.mp4']
keyfrmae = 1
cap = cv2.VideoCapture(fileList[2])
ret, lastframe = cap.read()
diff_frame_list=[]
while(cap.isOpened()):

    ret, frame = cap.read()
    if not ret:
        break
    diff_frame=diff_image_histogram(lastframe,frame)/frame.size
    diff_frame_list.append(diff_frame)
    lastframe = frame
    if cap.get(1)%100==0:
        print cap.get(1), '/', cap.get(7)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

plt_brokenLine(np.arange(len(diff_frame_list)),diff_frame_list)
cap.release()
cv2.destroyAllWindows()
