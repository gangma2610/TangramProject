#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-06 13:44
# @Author  : Lynn
# @Site    : 
# @File    : collect_data.py
# @Software: PyCharm

import cv2
import csv
import numpy as np
import math
from RecognitionRotate import ColorContourRecognition, ShapeRecognition

color_dict = {  'pink':0, 'red':1, 'orange':2, 'yellow':3,
                'green':4, 'blue':5, 'purple':6,
            }

index_color_dict = {
    0:'pink-red', 1:'pink-orange', 2:'pink-yellow', 3:'pink-green', 4:'pink-blue',
    5:'pink-purple', 6:'red-orange', 7:'red-yellow', 8:'red-green', 9:'red-blue', 10:'red-purple',
    11:'orange-yellow', 12:'orange-green', 13:'orange-blue', 14:'orange-purple',
    15:'yellow-green', 16:'yellow-blue', 17:'yellow-purple',
    18:'green-blue', 19:'green-purple', 20:'blue-purple',
}

header_list =[
    'pink-red', 'pink-orange', 'pink-yellow', 'pink-green', 'pink-blue',
    'pink-purple', 'red-orange', 'red-yellow', 'red-green', 'red-blue', 'red-purple',
    'orange-yellow', 'orange-green', 'orange-blue', 'orange-purple',
    'yellow-green', 'yellow-blue', 'yellow-purple',
    'green-blue', 'green-purple', 'blue-purple',
    'average', 'std', 'var'
]

def get_centers(image, flag=1):
    center_pos_list = []
    for i in [0, 1, 2, 3, 4, 5, 6]:
        if i == 0:
            color = 'pink'
            shape = 'triangle'
        elif i == 1:
            color = 'red'
            shape = 'triangle'
        elif i == 2:
            color = 'orange'
            shape = 'triangle'
        elif i == 3:
            color = 'yellow'
            shape = 'parallelogram'
        elif i == 4:
            color = 'green'
            shape = 'triangle'
        elif i == 5:
            color = 'blue'
            shape = 'square'
        else:
            color = 'purple'
            shape = 'triangle'

        mould = ShapeRecognition(flag, image)
        mould.completeRecognition(color, shape)
        (y, x) = (mould.centerP.x, mould.centerP.y)
        center_pos_list.append((x, y))

    return np.array(center_pos_list)


def cal_errors(list, rate):
    # print(list)
    distances = []
    for i in range(0, 7):
        for j in range(i + 1, 7):
            dis = math.sqrt(((list[i][0]-list[j][0])/rate)*((list[i][0]-list[j][0])/rate) \
                                  + ((list[i][1]-list[j][1])/rate)*((list[i][1]-list[j][1])/rate))
            # print("({}, {}) = {} ".format(i, j, dis))
            distances.append(round(dis, 2))
    return np.array(distances)

def get_result(e_image_list, real_image_list):
    # 计算距离
    e_distances = cal_errors(e_image_list, 3)
    real_distances = cal_errors(real_image_list, 256/70)
    # 电子图和实物图之间的距离差的绝对值
    result = np.abs(real_distances - e_distances)
    # result = real_distances - e_distances
    print('************************************************************')
    print('\n电子图中心点坐标:\n', e_image_list)
    print('\n实物图图中心点坐标：\n', real_image_list)
    print('\ne_distances:\n', e_distances)
    print('\nreal_distances: ', real_distances)
    print('\nresult: \n')

    for i in range(21):
        print(index_color_dict[i], ': ', round(result[i], 2))
    print('\n均值：', round(np.mean(result), 2))
    print('\n方差：', round(np.var(result), 2))
    print('\n标准差：', round(np.std(result), 2))
    print('\n************************************************************\n')
    write_result = result
    write_result = np.round(write_result, 2)
    write_result = np.append(write_result, round(np.mean(result), 2))
    write_result = np.append(write_result, round(np.var(result), 2))
    write_result = np.append(write_result, round(np.std(result), 2))
    # add_to_csv(write_result)
    # print('write result: ', len(write_result))
    return write_result



def add_to_csv(datas, path='results.csv'):
    out = open(path, 'a', newline='')
    csv_writer = csv.writer(out, dialect='excel')
    # csv_writer = csv.writer(path, 'w', newline='')
    # print(len(header_list))
    csv_writer.writerow(datas)
    pass




if __name__ == '__main__':
    # data = []
    # write_to_csv(data)
    # 添加头
    # add_to_csv(header_list)
    # print('head list: ', len(header_list))
    e_image = cv2.imread('images/mould/people02.jpg')
    e_image_list = get_centers(e_image, 1)
    e_distances = cal_errors(e_image_list, 3)

    print('********************************')
    print('\n\t图1\n')
    real_image = cv2.imread('/Users/lynn/Desktop/img/1.jpg')
    real_image_list = get_centers(real_image, 0)
    get_result(e_image_list, real_image_list)
    #
    print('********************************')
    print('\n\t图2\n')
    real_image = cv2.imread('/Users/lynn/Desktop/img/2.jpg')
    real_image_list = get_centers(real_image, 0)
    get_result(e_image_list, real_image_list)
    #
    print('********************************')
    print('\n\t图3\n')
    real_image = cv2.imread('/Users/lynn/Desktop/img/3.jpg')
    real_image_list = get_centers(real_image, 0)
    get_result(e_image_list, real_image_list)



