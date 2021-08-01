# -*- coding: utf-8 -*-

"""
    @project: Sorting-Algorithms
    @version: v1.0.0
    @file: main.py
    @brief: main file
    @software: PyCharm
    @author: Kai Sun
    @email: autosunkai@gmail.com
    @date: 2021/8/1 21:08
    @updated: 2021/8/1 21:08
"""
from bubble_sort import *

if __name__ == '__main__':
    sort = bubble_sort_pro
    arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    print('Raw:', arr)
    arr = sort(arr)
    print('Sorted:', arr)
