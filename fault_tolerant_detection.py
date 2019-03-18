#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/7 14:41
# @Author  : Lynn
# @Site    : 
# @File    : fault_tolerant_detection.py
# @Software: PyCharm

from items import Tangram, STACK, SET
from RecognitionRotate import ColorContourRecognition, ShapeRecognition

def puzzled_detection(real_image):
    temp = []
    for item in SET: #遍历检查已拼好的木块
        real = ShapeRecognition(0, real_image)
        real.completeRecognition(item.color, item.shape)
        # 如果检测失败，将item压入栈中，同时从SET中移除item
        if real.cnt_num != 1:
            print('没有： ', item.color, item.shape)
            STACK.push(item)
            temp.append(item)

        else:
            print('检测到： ', item.color, item.shape)

    # 对未检测到的木块进行排序
    temp.sort(key=lambda item:(item.pos_y, item.pos_x))
    for item in temp:
        SET.remove(item)

