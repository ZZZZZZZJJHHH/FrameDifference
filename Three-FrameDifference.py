import cv2
import os

# 数据集的根目录
rootDir = '/Users/mac/数据集/dataset2012/highway/input'
# 对所有文件排序
lists = sorted(os.listdir(rootDir))
# 第一帧
firstFrame = []
# 第二帧
secondFrame = []
for list in lists:
    path = os.path.join(rootDir, list)
    # 当前帧
    current = cv2.imread(path, 0)
    if not len(firstFrame):
        firstFrame = current
        continue
    if not len(secondFrame):
        secondFrame = current
        continue
    else:
        # 第一帧和第二帧差分
        foreground1 = cv2.absdiff(secondFrame, firstFrame)
        # 二值化
        ret, thresh1 = cv2.threshold(foreground1, 25, 255, cv2.THRESH_BINARY)
        # 当前帧和第二帧差分
        foreground2 = cv2.absdiff(current, secondFrame)
        # 二值化
        ret, thresh2 = cv2.threshold(foreground2, 25, 255, cv2.THRESH_BINARY)
        # 图像相交
        thresh = cv2.bitwise_and(thresh1, thresh2)

        firstFrame = secondFrame
        secondFrame = current

        cv2.imshow('input', current)
        cv2.imshow('foreground', thresh)
        cv2.waitKey(33)
