# -*- coding: utf-8 -*-

"""
    @project: Sorting-Algorithms
    @version: v1.0.0
    @file: bubble_sort.py
    @brief: Bubble Sort
    @software: PyCharm
    @author: Kai Sun
    @email: autosunkai@gmail.com
    @date: 2021/8/1 20:29
    @updated: 2021/8/1 21:08
"""


def bubble_sort(arr):
    for i in range(len(arr)):               # 循环第 i 趟
        for j in range(len(arr) - i - 1):   # j 为下标
            if arr[j] > arr[j + 1]:         # 如果这个数大于后面的数就交换两者的位置
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def bubble_sort_pro(arr):
    for i in range(len(arr)):               # 循环第 i 趟
        flag = False                        # 每次都初始化标记
        for j in range(len(arr) - i - 1):   # 如果这个数大于后面的数就交换两者的位置
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = True                 # 有逆序就设置标记
        if not flag:                        # 标记没有变化就退出循环
            break
    return arr
