import cv2
import os

# 数据集的根目录
rootDir = '/Users/mac/数据集/dataset2012/highway/input'
# 对所有文件排序
lists = sorted(os.listdir(rootDir))
# 前一帧
previousFrame = []
for list in lists:
    path = os.path.join(rootDir, list)
    # 当前帧
    current = cv2.imread(path, 0)
    if not len(previousFrame):
        previousFrame = current
    else:
        # 差分
        foreground = cv2.absdiff(current, previousFrame)
        previousFrame = current
        # 二值化，阈值设为25，可修改
        ret, thresh = cv2.threshold(foreground, 25, 255, cv2.THRESH_BINARY)
        cv2.imshow('input', current)
        cv2.imshow('foreground', thresh)
        cv2.waitKey(33)
