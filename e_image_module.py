#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 19:13
# @Author  : Lynn
# @Site    : 
# @File    : e_image_module.py
# @Software: PyCharm
'''
识别电子图中的七个七巧板，并按七巧板坐标进行排序，来实现按序拼图的功能。
将排好序的七个七巧板放入栈STACK中。
'''
import cv2
from items import STACK
from items import Tangram
from RecognitionRotate import ColorContourRecognition, ShapeRecognition

def clear_stack():
    while STACK.is_empty() == False:
        STACK.pop()

def get_list(e_image):
    info = []
    # for i in range(0, 7):
    # for i in [3]:
    for i in [ 0, 1, 2, 3, 4, 5, 6]:
        if i == 0:
            color = 'pink'
            shape = 'triangle'
        elif i == 1:
            color = 'red'
            shape = 'triangle'
        elif i == 2:
            color = 'orange'
            shape = 'triangle'
        elif i == 3:
            color = 'yellow'
            shape = 'parallelogram'
        elif i == 4:
            color = 'green'
            shape = 'triangle'
        elif i == 5:
            color = 'blue'
            shape = 'square'
        else:
            color = 'purple'
            shape = 'triangle'

        mould = ShapeRecognition(1, e_image)
        mould.completeRecognition(color, shape)
        (y, x) = (mould.centerP.x, mould.centerP.y)
        # print(color, shape, x, y)

        info.append(Tangram(color, shape, x, y))
        # print(len(info))
    return info

def set_stack(e_image):
    #清空栈
    clear_stack()
    info = get_list(e_image)
    #根据坐标对每块七巧板进行排序
    info.sort(key=lambda item:(item.pos_y, item.pos_x))
    for item in info:
        STACK.push(item)




if __name__ == '__main__':
    e_image = cv2.imread('images/mould/test.jpg')
    # cv2.imshow('image', e_image)
    # cv2.waitKey(0)
    # tang = get_list(e_image)
    # print('printing...')
    # print(type(tang))
    # tang.sort(key=lambda item:(item.pos_y, item.pos_x))
    # for i, item in enumerate(tang):
    #     print('{0}, {1}, ({2}, {3})'.format(item.color, item.shape, item.pos_x, item.pos_y))
    set_stack(e_image)
    while STACK.is_empty() == False:
        top = STACK.pop()
        print('{0}, {1}, ({2}, {3})'.format(top.color, top.shape, top.pos_x, top.pos_y))

