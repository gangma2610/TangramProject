#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/7 14:41
# @Author  : Lynn
# @Site    : 
# @File    : fault_tolerant_detection.py
# @Software: PyCharm
from items import Tangram, STACK, SET
from RecognitionRotate import ColorContourRecognition, ShapeRecognition

def puzzled_detection(e_image, real_image):
    for item in SET:
        real = ShapeRecognition(0, real_image)
        real.completeRecognition(item.color, item.shape)