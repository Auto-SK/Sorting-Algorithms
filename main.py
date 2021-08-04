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
from selection_sort import *
from insertion_sort import *
from shell_sort import *
from merge_sort import *
from quick_sort import *
from heap_sort import *

if __name__ == '__main__':
    sort = heap_sort
    arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    print('Raw:', arr)
    arr = sort(arr)
    print('Sorted:', arr)
