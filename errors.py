#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 20:32
# @Author  : Lynn
# @Site    : 
# @File    : errors.py
# @Software: PyCharm

STATE = 0

NO_SHAPE_ERROR = 1      # 没有检测到形状

MULTI_SHAPE_ERROR = 2   # 检测到多个形状

WAIT_TIMES_ERROR = 3    # 容错次数状态

TO_MOVE_ERROR = 4       # 容错后移动状态

MOVED_STILL_ERROR = 5

MOVE_TO_INIT_POS = -1

#
# def duges(state):
#     if STATE == NO_SHAPE_ERROR:
#         STATE = WAIT_TIMES_ERROR
#
#     elif STATE == MULTI_SHAPE_ERROR:
#         STATE = WAIT_TIMES_ERROR
#
#     elif STATE == WAIT_TIMES_ERROR:
#         pass