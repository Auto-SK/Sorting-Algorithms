# -*- coding: utf-8 -*-

"""
    @project: Sorting-Algorithms
    @version: v1.0.0
    @file: insertion_sort.py
    @brief: Insertion Sort
    @software: PyCharm
    @author: Kai Sun
    @email: autosunkai@gmail.com
    @date: 2021/8/1 23:08
    @updated: 2021/8/1 23:08
"""


def insertion_sort(arr):
    for i in range(1, len(arr)):            # 将 i 看作摸到的牌的下标
        value = arr[i]                      # 将摸到的牌储存到 value
        j = i - 1                           # 将 j 看做手里的牌的下标
        while j >= 0 and arr[j] > value:    # 如果手里的牌大于摸到的牌
            arr[j + 1] = arr[j]             # 将手里的牌右移一个位置
            j -= 1                          # 下标 j 左移一个位置
        arr[j + 1] = value                  # 将摸到的牌插入到 j + 1 位置
    return arr
