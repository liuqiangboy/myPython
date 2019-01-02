# -*- coding:utf-8 -*-
import numpy as np
import cv2
import os
from time import clock
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
    src_2 = convertImage(src_2)
    src_1 = src_1.astype(np.int)
    src_2 = src_2.astype(np.int)
    diff = abs(src_1 - src_2)
    res=np.sum(diff.astype(np.uint8))
    return res
if __name__=='__main__':
    start=clock()
    fileList=[
              '/Users/liuqiang/Downloads/视频镜头分割及关键帧提取技术的研究与实现416/表演.mp4',
              '/Users/liuqiang/Downloads/视频镜头分割及关键帧提取技术的研究与实现416/动漫.mp4',
              '/Users/liuqiang/Desktop/镜头分割/功守道.mp4',
            '/Users/liuqiang/Downloads/视频镜头分割及关键帧提取技术的研究与实现416/猎场片花.mp4',
              ]
    keyfrmae = []
    cap = cv2.VideoCapture(fileList[3])
    ret, lastframe = cap.read()
    while(cap.isOpened()):
        ret, frame = cap.read()
        if not ret:
            break
        diff_frame=diff_image_histogram(lastframe,frame)/frame.size
        if  diff_frame> 100:
            keyfrmae.append(int(cap.get(0))/1000)

        lastframe = frame
        if cap.get(1)%100==0:
            print cap.get(1), '/', cap.get(7)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    print(keyfrmae)
    print('time cost:',clock()-start)

