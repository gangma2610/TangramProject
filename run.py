#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/8 12:12
# @Author  : Lynn
# @Site    : 
# @File    : run.py
# @Software: PyCharm

from decision import *

def main():
    assistant_functions.delete_image('images/catching/')
    start = time.time()
    decesion = Decision()
    #
    e_image = cv2.imread('images/mould/5.jpg')

    decesion.do_puzzles(e_image)

    print('end!!!')
    end = time.time()
    print('time: {}'.format(int(end - start)))


if __name__ == '__main__':
    main()
