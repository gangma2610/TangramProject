#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/13 12:56
# @Author  : Lynn
# @Site    : 
# @File    : assistant.py
# @Software: PyCharm
import os
import time
import shutil
############################################################################################
def delete_image(delDir='.'):
    '''
    删除指定目录下生成的所有图片。

    参数：
    ----------
    :param delDir:  指定的目录

    返回值：
    ----------
    :return:        None
    '''
    # delList = []
    # delLis = os.listdir(delDir)
    for root, dirs, files in os.walk(delDir):
        for name in files:
            if(name.endswith('.jpg')):
                os.remove(os.path.join(root, name))


def save_collected_images(source_path='images/catching/', target_path= '../图像采集/'):
    # localtime = time.localtime(time.time())
    path_time = time.strftime('%Y%m%d%H%M%S', time.localtime())
    new_path = target_path + path_time + '/'
    if not os.path.exists(new_path):
        os.makedirs(new_path)

    for root, dirs, files in os.walk(source_path):
        for name in files:
            if name.endswith('.jpg'):
                shutil.move(os.path.join(root,name), new_path)


if __name__ == '__main__':
    save_collected_images()
