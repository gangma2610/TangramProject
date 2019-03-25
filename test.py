#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/8 15:51
# @Author  : Lynn
# @Site    : 
# @File    : test.py
# @Software: PyCharm
from robot_controller import *
import time
import numpy as np
import os
################################################################



def delete_image(delDir = '.'):
    # delList = []
    # delLis = os.listdir(delDir)
    for root, dirs, files in os.walk(delDir):
        for name in files:
            if(name.endswith('.jpg')):
                os.remove(os.path.join(root, name))

def main():
    """
    机械臂移动以及设置速度过程中无需自己添加延迟函数，但手爪
    闭合以及张开需自己根据实际情况添加延迟函数。
    """
    # delete_image()
    # tlen = 128
    init_pos = [400, 100, 510, 180, 0, 0]
    test_pos = [400, 100, 360, 180, 0, 0]
    init_pos_axis = [0, 0, 0, 0, 0, 0]
    detect_pos =  [400, -155, 400, 180, 0, 0]
    # test_pos = [510, 260, 175, 180, 0, 0]
    # prea = np.array([0, 56, -17, 0, 24, 0])
    set_pos = [464.0, -142.67, 153.56,180, 0, 0]

    robot_instance = RobotController()

    # 笛卡尔坐标运动
    control = 1


    if control ==0 :
        robot_instance.move_axis(init_pos_axis) # 回零
    elif control == 1:
        robot_instance.move_car(init_pos)  # 项目的初始坐标
    elif control == 2:
        robot_instance.move_car(test_pos)
    elif control == 3:
        robot_instance.move_car(detect_pos)
    elif control == 4:
        robot_instance.control_paw(4)  # 张开
    elif control == 5:
        robot_instance.control_paw(5)  # 闭合
    else:
        robot_instance.move_car(set_pos)
        pass
    # robot_instance.move_car(detect_pos)
    # robot_instance.move_car(test_pos)
    # 关节坐标运动
    # robot_instance.move_axis(init_pos_axis)

    # 偏移量运动
    # robot_instance.move_car_by_offset(offset_C = 180) # 笛卡尔偏移量
    # robot_instance.move_axis_by_offset(offset_a6 = 180) # 关节偏移量

    # 控制手爪闭合和张开
    # robot_instance.control_paw(5) # 闭合
    # robot_instance.control_paw(4) # 张开

    # 设置机械臂运动速度
    # robot_instance.set_speed(1)

    # 获取机械臂当前坐标
    # print(robot_instance.get_current_car_pos()) # 笛卡尔坐标
    # print(robot_instance.get_current_axis_pos()) # 关节坐标

    robot_instance.close()

if __name__ == '__main__':
    main()