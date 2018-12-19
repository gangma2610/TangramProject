#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 20:32
# @Author  : Lynn
# @Site    : 
# @File    : errors.py
# @Software: PyCharm

STATE = 0

OK = 0

ERROR_NO_SHAPE = 1      # 没有检测到形状

ERROR_MULTI_SHAPE = 2   # 检测到多个形状

ERROR_WAIT_TIMES = 3    # 容错次数状态

ERROR_TO_MOVE = 4       # 容错后移动状态

ERROR_MOVED = 5

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