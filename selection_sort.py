# -*- coding: utf-8 -*-

"""
    @project: Sorting-Algorithms
    @version: v1.0.0
    @file: selection_sort.py
    @brief: Selection Sort
    @software: PyCharm
    @author: Kai Sun
    @email: autosunkai@gmail.com
    @date: 2021/8/1 21:41
    @updated: 2021/8/1 21:41
"""


def selection_sort(arr):
    for i in range(len(arr) - 1):           # 循环第 i 趟
        min_index = i                       # 记录最小数的下标
        for j in range(i + 1, len(arr)):    # j 为下标
            if arr[j] < arr[min_index]:     # 如果这个数小于记录的最小数则更新最小数的下标
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # 将已排序序列末尾的数和最小数交换
    return arr
