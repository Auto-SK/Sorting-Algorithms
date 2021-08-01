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
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def bubble_sort_pro(arr):
    for i in range(len(arr)):
        flag = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = True
        if not flag:
            break
    return arr
