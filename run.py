#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/8 12:12
# @Author  : Lynn
# @Site    : 
# @File    : run.py
# @Software: PyCharm

from decision import *

def main():
    """
    测试机器人逐步逼近目标。

    返回值：
    ----------
    :return: None
    """
    # assistant_functions.delete_image('images/catching/')
    assistant_functions.save_collected_images('images/catching/')
    start = time.time()
    e_image = cv2.imread('images/mould/cat01.jpg')
    decesion = Decision(e_image)  # 传入电子图
    #

    e_image_module.set_stack(e_image)
    decesion.do_puzzles()

    print('end!!!')
    end = time.time()
    print('time: {}'.format(int(end - start)))


if __name__ == '__main__':
    main()
