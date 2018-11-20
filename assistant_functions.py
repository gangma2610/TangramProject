#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/13 12:56
# @Author  : Lynn
# @Site    : 
# @File    : assistant_functions.py
# @Software: PyCharm
import os
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