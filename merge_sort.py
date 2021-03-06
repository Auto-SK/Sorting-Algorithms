# -*- coding: utf-8 -*-

"""
    @project: Sorting-Algorithms
    @version: v1.0.0
    @file: merge_sort.py
    @brief: Merge Sort
    @software: PyCharm
    @author: Kai Sun
    @email: autosunkai@gmail.com
    @date: 2021/8/3 22:56
    @updated: 2021/8/3 22:56
"""


def merge_sort(arr):
    def mergesort(l, r):
        # 终止条件
        if l >= r:
            return
        # 递归划分
        m = ((r - l) >> 1) + l
        mergesort(l, m)
        mergesort(m + 1, r)
        # 合并阶段
        i, j = l, m + 1
        tmp[l: r + 1] = arr[l: r + 1]
        for k in range(l, r + 1):
            if i > m or (j <= r and tmp[i] > tmp[j]):
                arr[k] = tmp[j]
                j += 1
            else:
                arr[k] = tmp[i]
                i += 1
    tmp = [0] * len(arr)
    mergesort(0, len(arr) - 1)
    return arr

