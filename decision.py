#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/8 10:42
# @Author  : Lynn
# @Site    : 
# @File    : decision.py
# @Software: PyCharm
import numpy as np
import cv2
import math
import pickle
import matplotlib.pyplot as plt

import time
import os
import sys
import math

from robot_controller import RobotController
from RecognitionRotate import ColorContourRecognition, ShapeRecognition, Rotate
import e_image_module
import assistant_functions

from items import STACK, SET

import fault_tolerant_detection
############################################################################################
class Decision:
    def __init__(self, e_image, camera_flag=0, frame_width=1024, frame_height=768):
        """
        参数：
        ----------
        :param camera_flag: int
                摄像头端口（0，1）
        :param frame_width: int
                摄像头像素宽度
        :param frame_height: int
                摄像头像素高度
        """
        self._e_image = e_image

        self._num_pic = 0
        self._init_carpos = [400, 100, 510, 180, 0, 0] #初始笛卡尔坐标
        self._detect_carpos = [400, -155, 400, 180, 0, 0]

        self._robot_instance = RobotController()
        # self._robot_instance.send_OK()

        print('启动摄像头...')
        self._cap = cv2.VideoCapture(camera_flag)
        self._cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
        self._cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

        ret, img = self._cap.read()
        print('摄像头就绪.')



    def __del__(self):
        """
        在析构函数中关闭机械臂的TCP连接、释放摄像头资源。
        """
        self._robot_instance.close()
        self._cap.release()



    def delay(self, t=1):
        '''

        延迟函数。

        参数：
        ----------
        :param t: 延迟时间

        返回值：
        ----------
        :return:  None
        '''
        time.sleep(t)



    def get_image_vector(self, image, color, shape):
        """
        获取移动方向的矢量坐标。

        参数：
        ----------
        :param image: Image
                图像
        :param color: string
                木块颜色
        :param shape: string
                木块形状

        返回值：
        ----------
        :return: tuple
                (y,x)移动方向的矢量坐标
        """

        # ld = Analysis()
        # vec = ld.analy(color, shape, image)
        real = ShapeRecognition(0, image)
        real.completeRecognition(color, shape)
        return real.centerVector



    def gradually_approach(self, color, shape, offset, error):
        '''
        逐步逼近目标。

        参数：
        ----------
        :param color: str
                目标木块的颜色
        :param shape:  str
                目标木块的形状
        :param offset: float
                偏移量，每次逼近目标时机械臂移动的步长
        :param error: int
                误差，逼近过程中所容忍的误差（像素）,目标中心点离图像中心点的像素距离不超过误差，即停止逼近

        返回值：
        ----------
        :return:    None
        '''
        # 逐步逼近x轴
        print('***************************************')
        print('move_car for x...')
        flag = True
        while flag:
            # catch an image
            ret, img = self._cap.read()

            cv2.imwrite('images/catching/{0}.jpg'.format(self._num_pic), img)
            self._num_pic += 1

            y, x = self.get_image_vector(img, color, shape)
            print('vector: ({0},{1})'.format(x, y))

            if math.fabs(x) >= error and math.fabs(y) >= error:
                print('move: x, y')
                x_offset = y_offset = offset
                if x < 0:
                    x_offset = -x_offset
                if y < 0:
                    y_offset = -y_offset

                self._robot_instance.move_car_by_offset(offset_x=x_offset, offset_y=y_offset)
                # self.delay()

            elif math.fabs(x) >= error:
                print('move: x')
                x_offset = offset
                if x < 0:
                    x_offset = -x_offset

                self._robot_instance.move_car_by_offset(offset_x=x_offset)
                # self.delay()

            elif math.fabs(y) >= error:
                print('move: y')
                y_offset = offset
                if y < 0:
                    y_offset = -y_offset

                self._robot_instance.move_car_by_offset(offset_y=y_offset)
                # self.delay()

            else:
                flag = False



    def locating(self, color, shape='triangle'):
        '''
        逐步逼近定位指定颜色和形状的木块。

        参数：
        ----------
        :param color: str
                木块颜色
        :param shape: str
                木块形状

        返回值：
        ----------
        :return:    None
        '''
        # self._robot_instance.control_paw(4)
        # self.delay(0.5)
        # self._robot_instance.move_car(self._init_carpos) #机械臂移动到初始位置
        # self.delay(10)

        # 第一次逼近目标
        print('first time approach...')

        print('offset: %d, error: %d' % (10, 80))
        self.gradually_approach(color, shape, 10, 80)
        print('offset: %d, error: %d' % (5, 30))
        self.gradually_approach(color, shape, 5, 30)

        print('offset: %d, error: %d' % (2, 5))
        self.gradually_approach(color, shape, 2, 5)

        self._robot_instance.move_car_by_offset(offset_z=-100)  # z = 410
        # self.delay(5)
        # 第二次逼近目标
        print('second time approaching...')

        print('offset: %d, error: %d' % (10, 80))
        self.gradually_approach(color, shape, 10, 80)
        print('offset: %d, error: %d' % (5, 30))
        self.gradually_approach(color, shape, 5, 30)

        print('offset: %d, error: %d' % (1, 4))
        self.gradually_approach(color, shape, 1, 4)

        self._robot_instance.move_car_by_offset(offset_z=-50)  # z= 360
        # self.delay(5)
        # 第三次逼近目标
        print('third time approaching...')

        print('offset: %d, error: %d' % (10, 80))
        self.gradually_approach(color, shape, 10, 80)
        print('offset: %d, error: %d' % (5, 30))
        self.gradually_approach(color, shape, 5, 30)

        print('offset: %d, error: %d' % (1, 4))
        self.gradually_approach(color, shape, 1, 4)
        # 定位逼近完成，接下来将手爪移至木块上方，计算旋转角度，并抓取目标



    def cal_target_car_pos(self, x, y, x0= 550, y0=0, height=167):
        '''
        计算当前抓取的木块在拼图区域的坐标。

        参数：
        ----------
        :param x: int
                像素坐标x(图像坐标系中的y)
        :param y: int
                像素坐标y(图像坐标系中的x）
        :param x0: float
                拼图区域坐标系原点在世界坐标系中的x坐标(精度：两位小数)
        :param y0: float
                拼图区域坐标系原点在世界坐标系中的y坐标(精度：两位小数)
        :param height: float
                手臂的高度(精度：两位小数)

        返回值：
        ----------
        :return: tuple
                对应拼图区域的笛卡尔坐标((x,y,z,A,B,C), 精度：两位小数)
        '''
        carpos = [round(x0 - x / 3, 2), round(y0 - y / 3, 2), height, 180, 0, 0]
        return carpos


    def get_angle(self, real_image, color, shape):
        """
        计算旋转角度。
        :param real_image:  实物图
        :param color:       颜色
        :param shape:       形状

        :return:            旋转角度
        """
        mould = ShapeRecognition(1, self._e_image)
        mould.completeRecognition(color, shape)
        real = ShapeRecognition(0, real_image)
        real.completeRecognition(color, shape)
        rotate = Rotate()
        ang, flag = rotate.getRotateAngle(real, mould, shape)
        if flag == True:
            ang = -ang
        return ang



    def grab_tangram(self, color, shape, x_distance=44, y_distance = 6.5, height=164): #height = 167
        """
        目标定位到视野中心后，将手爪移至目标上方，计算旋转角度，然后抓取目标，进行旋转。

        参数：
        ----------
        :param data_mould: tangram_data
                七巧板数据信息对象
        :param m: int
                第m个木块
        :param distance: float
                手爪中心到摄像头中心距离
        :param height: float
                抓取目标时手爪高度

        返回值：
        ----------
        :return:    None
        """
        # 计算旋转角度
        ret, real_img = self._cap.read()
        # cv2.imwrite('angle.jpg', img)
        # ang = rotate_test.get_rotate_angle(data_mould, img, m)
        ang = self.get_angle(real_img, color, shape)

        # 计算矫正后的手臂坐标，并将爪子定位到目标上方。
        # robot.move_car_by_offset(offset_x=distance)
        self._robot_instance.move_car_by_offset(offset_x=x_distance, offset_y=y_distance)
        # self.delay(5)

        if ang > 180 or ang < -180:
            print('旋转角度超出范围: %.2f !!!!' % ang)
            sys.exit()

        # 降低高度，以便抓取目
        self._robot_instance.move_car_by_offset(offset_z=-196)  # z = 164
        # self.delay(5)
        # 抓取目标
        self._robot_instance.control_paw(5)
        self.delay(12)  # time = 10
        # 机械臂手爪上升至第三次逼近高度
        self._robot_instance.move_car_by_offset(offset_z=193)  # z = 360
        # self.delay(5)

        return ang


    def processing(self, color, shape, x, y):
        """
        拼指定颜色和形状的拼图。

        参数：
        ----------
        :param color:   颜色
        :param shape:   形状
        :param x:       七巧板质心x坐标（机械臂世界坐标系下）
        :param y:       七巧板质心y坐标（机械臂世界坐标系下）

        返回值：
        ----------
        :return:    None
        """
        print('===================================================')

        # step1: 获取电子图相应目标信息，并计算拼图区域对应坐标
        # mould = ShapeRecognition(1, self._e_image)
        # mould.completeRecognition(color, shape)
        # (y, x) = (mould.centerP.x, mould.centerP.y)
        # shape, color, (y, x) = data_mould.no_shape[str(m)][:3]
        # print(shape, color, (x, y))
        print('E-Image：',shape, color, (x, y))

        # 计算拼图区域对应坐标
        target_pos = self.cal_target_car_pos(x=x, y=y)
        # step2: 定位指定颜色和形状的木块
        self.locating(color, shape)
        # step3: 计算旋转角度，并抓取目标
        ang = self.grab_tangram(color, shape)
        # step4: 移至拼图对应区域,旋转相应角度，并释放目标
        target_pos[2] = 200
        print('移至拼图对应区域： ({0}, {1})'.format(target_pos[0], target_pos[1]))
        self._robot_instance.move_car(target_pos)  # z = 200
       # self.delay(7)

        # 旋转角度
        print('旋转 %.2f度...' % ang)
        self._robot_instance.move_car_by_offset(offset_C=round(ang, 2))
        # self.delay(11)
        print('z轴降低 %d mm，高度：%d ' % (31, 170))
        self._robot_instance.set_speed(1)
        self._robot_instance.move_car_by_offset(offset_z=-35)  # z = 172 #z=165
        self._robot_instance.set_speed(4)
        # self.delay()

        # 释放目标
        self._robot_instance.control_paw(4)
        self.delay(5)

        # 移到检测位置
        self._robot_instance.move_car(self._detect_carpos)
        # 容错检测
        time.sleep(2)
        ret, real_img = self._cap.read()
        cv2.imwrite('images/catching/{0}.jpg'.format(self._num_pic), real_img)
        self._num_pic += 1
        fault_tolerant_detection.puzzled_detection(real_img)
        # self._robot_instance.control_paw(4)
        # self.delay(0.5)
        self._robot_instance.move_car(self._init_carpos)  # 机械臂移动到初始位置


    def do_puzzles(self):
        """
        拼拼图。


        返回值：
        ----------
        :return     None
        """
        self._robot_instance.set_speed(4)

        while STACK.is_empty() == False:
            top = STACK.pop() #出栈，拼接栈顶七巧板
            SET.add(top) # 加入已拼接队列
            # self.processing(e_image, color, shape)
            self.processing(top.color, top.shape, top.pos_x, top.pos_y)


def main():
    """
    测试机器人逐步逼近目标。

    返回值：
    ----------
    :return: None
    ----------
    """
    # assistant_functions.delete_image('images/catching/')
    assistant_functions.save_collected_images('images/catching/')
    start = time.time()
    e_image = cv2.imread('images/mould/cat01.jpg')
    decesion = Decision(e_image) # 传入电子图
    #

    e_image_module.set_stack(e_image)
    decesion.do_puzzles()

    print('end!!!')
    end = time.time()
    print('time: {}'.format(int(end - start)))



if __name__ == '__main__':
    main()
