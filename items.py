#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 18:27
# @Author  : Lynn
# @Site    : 
# @File    : items.py
# @Software: PyCharm
from stack import Stack

#########################################################

STACK = Stack() #存放待拼接的七巧板信息

SET = set([]) #记录已经拼接好的七巧板信息

#########################################################
class Tangram:
    '''定义七巧板属性类，包含七巧板的颜色，形状以及中心坐标x和y'''
    def __init__(self, color, shape, x, y):
        self.color = color
        self.shape = shape
        self.pos_x = x
        self.pos_y = y

