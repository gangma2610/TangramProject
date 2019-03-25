#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-20 22:10
# @Author  : Lynn
# @Site    : 
# @File    : statistics.py
# @Software: PyCharm

import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import matplotlib as mpl


header_list =[
    'pink-red', 'pink-orange', 'pink-yellow', 'pink-green', 'pink-blue',
    'pink-purple', 'red-orange', 'red-yellow', 'red-green', 'red-blue', 'red-purple',
    'orange-yellow', 'orange-green', 'orange-blue', 'orange-purple',
    'yellow-green', 'yellow-blue', 'yellow-purple',
    'green-blue', 'green-purple', 'blue-purple',
    'average', 'var', 'std'
]

def draw_line_chart():
    data = pd.read_csv('res/results.csv', delimiter=',')
    print('shape = ', data.shape)
    dt_avg = np.array(data['average'])
    dt_var = np.array(data['var'])
    dt_std = np.array(data['std'])
    avg = np.average(dt_avg)
    print('avg = ', avg)
    print('均值: \n', dt_avg)
    print('方差: \n', dt_var)
    print('标准差:\n', dt_std)

    print(data.values)

    all_std = np.std(data.values)
    # all_data = data.values()[:, :]
    # print(all_data)
    # print('整体标准差 = ', np.std(np.array(all_data)))
    # 均值，方差，标准差的折线图
    x = np.arange(1, data.shape[0] + 1)
    # np.set_printoptions(precision=3)
    # y = np.linspace(0, 2.8, 15)
    #
    # y = np.round(y, decimals=2)
    print(x)
    # print(y)

    plt.plot(x, dt_avg, 'r-', linewidth=2, label='Average in one trail')
    plt.plot(x, np.array([all_std]*data.shape[0]), 'm--', linewidth=1, label='Std in all trails')
    # plt.plot(x, dt_var, 'b-', linewidth=2, label='Var')
    plt.plot(x, np.array([avg] * len(dt_avg)), 'r--', linewidth=1, label='Average in all trails')
    plt.ylim(0, 4)
    plt.xlim(1, data.shape[0])
    plt.xlabel('Trails')
    plt.ylabel('Distances (mm)')
    plt.legend(loc='upper right')
    # plt.title('Results')
    plt.grid()
    plt.savefig('res/statistics.jpg')
    plt.show()

def draw_scatter_chart():
    data = pd.read_csv('res/results.csv', delimiter=',')
    print('shape = ', data.shape)
    dt_avg = np.array(data['average'])
    dt_var = np.array(data['var'])
    dt_std = np.array(data['std'])
    avg = np.average(dt_avg)
    print('avg = ', avg)
    print('均值: \n', dt_avg)
    print('方差: \n', dt_var)
    print('标准差:\n', dt_std)

    # 均值，方差，标准差的折线图
    x = np.arange(1, data.shape[0] + 1)
    plt.plot(x, dt_avg, 'rv')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    draw_line_chart()
    # draw_scatter_chart()

    # plt.scatter(x, dt_avg, c='')
    # data = pd.read_csv('res/results.csv', delimiter=',')
    # print('shape = ', data.shape)
    # dt_avg = np.array(data['average'])
    # dt_var = np.array(data['var'])
    # dt_std = np.array(data['std'])
    # avg = np.average(dt_avg)
    # print('avg = ', avg)
    # print('均值: \n', dt_avg)
    # print('方差: \n', dt_var)
    # print('标准差:\n', dt_std)
    #
    # N, M = 20, 20
    # t1 = np.linspace(0, 10, N)
    # t2 = np.linspace(0, data.shape[0] + 1, M)
    # x1, x2 = np.meshgrid(t1, t2)
    # x_test = np.stack((x1.flat, x2.flat), axis=1)




