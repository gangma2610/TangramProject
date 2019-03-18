#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 18:27
# @Author  : Lynn
# @Site    : 
# @File    : items.py
# @Software: PyCharm
from stack import Stack

#########################################################

STACK = Stack() # 存放待拼接的七巧板信息

SET = set([]) # 记录已经拼接好的七巧板信息

# E_IMAGE = None # 记录电子图

#########################################################
class Tangram:
    '''定义七巧板属性类，包含七巧板的颜色，形状以及中心坐标x和y'''
    def __init__(self, color, shape, x, y):
        self.color = color
        self.shape = shape
        self.pos_x = x
        self.pos_y = y


#########################################################
# 容错检测部分的状态量
STATE = 0

OK = 0

ERROR_NO_SHAPE = 1      # 没有检测到形状

ERROR_MULTI_SHAPE = 2   # 检测到多个形状

ERROR_WAIT_TIMES = 3    # 容错次数状态

ERROR_TO_MOVE = 4       # 容错后移动状态

ERROR_MOVED = 5

MOVE_TO_INIT_POS = -1

