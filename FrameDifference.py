import cv2
import os
rootDir = '/Users/mac/数据集/dataset2012/highway/input'
#对所有文件排序
lists = sorted(os.listdir(rootDir))
previousframe = []
for list in lists:
    path = os.path.join(rootDir, list)
    #当前帧
    current = cv2.imread(path, 0)
    if not len(previousframe):
        previousframe = current
    else:
        foreground = cv2.absdiff(current, previousframe)
        previousframe = current
        #阈值设为25，可修改
        ret,thresh = cv2.threshold(foreground,25,255,cv2.THRESH_BINARY)
        cv2.imshow('input', current)
        cv2.imshow('foreground',thresh)
        cv2.waitKey(33)
