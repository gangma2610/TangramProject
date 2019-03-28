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
import matplotlib.mlab as mlab


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

    plt.plot(x, dt_avg, 'r-', linewidth=1, label='Average in one trail')
    plt.plot(x, np.array([avg] * len(dt_avg)), 'r--', linewidth=1, label='Average in all trails')
    plt.plot(x, np.array([all_std]*data.shape[0]), 'm--', linewidth=1, label='Standard deviation in all trails')
    # plt.plot(x, dt_var, 'b-', linewidth=2, label='Var')

    plt.ylim(0, 5)
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

def draw_distribution():
    data = pd.read_csv('res/results.csv', delimiter=',')
    print('shape = ', data.shape)
    dt_avg = np.array(data['average'])
    print('均值: \n', dt_avg)


if __name__ == '__main__':
    # draw_line_chart()
    # draw_scatter_chart()
    # draw_distribution()

    # plt.scatter(x, dt_avg, c='')
    data = pd.read_csv('res/results.csv', delimiter=',')

    print('shape = ', data.shape)
    dt_avg = np.array(data['average'])
    # print(dt_avg.max())
    distribute = np.linspace(0.2, 3.2, 15+1)
    fenzu = pd.cut(data['average'].values, distribute)
    print('分组: \n', fenzu)
    # pinshu = fenzu.value_counts()
    # print(pinshu)
    # plt.hist(pinshu)
    # plt.show()
    plt.hist(data['average'], bins=15, facecolor='blue', alpha=0.75,rwidth=0.8)
    plt.savefig('res/hist.jpg')
    plt.show()

    # fenzu = pd.cut(dt_avg, distribute)
    # print('分组: \n', fenzu)
    #  pinshu = fenzu.value_counts() # series 区间-个数
    # y = np.array(pinshu.tolist()) / 100
    # print('y = \n', y)
    # print('code: \n', fenzu.codes) # 标签
    # print('categories: \n', fenzu.categories)
    # print('频数:\n', pinshu)
    # result = pinshu / 100
    # print('百分比:\n', result )
    # print('***************')
    # print('index:\n',pinshu.index.categories)
    # x = pinshu.index.categories
    # plt.hist(pinshu)
    # plt.show()






