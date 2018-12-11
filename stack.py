#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 18:42
# @Author  : Lynn
# @Site    : 
# @File    : stack.py
# @Software: PyCharm
# from items import Tangram

class Stack(object):
    '''
    封装栈：入栈，出栈，判断栈空，获取栈顶元素，获取栈的大小。
    '''
    def __init__(self):
        self.items = []

    def is_empty(self):
        '''
        判断栈是否空。

        返回值：
        ----------
        :return:  栈空：True，栈不空：False
        '''
        return self.items == []

    def peek(self):
        '''
        查看栈顶元素。

        返回值：
        ----------
        :return:  栈顶元素
        '''
        return self.items[-1]

    def size(self):
        '''
        返回栈中元素个数。

        返回值：
        ----------
        :return:   栈中元素个数
        '''
        return len(self.items)

    def push(self, item):
        '''
        将元素压入栈中。

        :param item:  入栈元素。

        返回值：
        ----------
        :return:    None
        '''
        self.items.append(item)

    def pop(self):
        '''
        弹出栈顶元素。

        返回值：
        ----------
        :return:    栈顶元素
        '''
        return self.items.pop()

# if __name__ == '__main__':
    # t1 = Tangram('yellow', 'd', 1, 2)
    # t2 = Tangram('red', 'r', 2,3)
    # t3 = Tangram('blue', 'b', 3, 4)
    #
    # my_stack = Stack()
    # my_stack.push(t1)
    # my_stack.push(t2)
    # print(my_stack.size())
    # # pop1 = my_stack.pop()
    # print(my_stack.peek().color, my_stack.peek().shape, my_stack.peek().pos_x, my_stack.peek().pos_y)
    # my_stack.push(t3)
    # print(my_stack.size())
    # my_stack.pop()
    # my_stack.pop()
    # print(my_stack.is_empty())
