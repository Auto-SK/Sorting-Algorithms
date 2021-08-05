# -*- coding: utf-8 -*-

"""
    @project: Sorting-Algorithms
    @version: v1.0.0
    @file: counting_sort.py
    @brief: Counting Sort
    @software: PyCharm
    @author: Kai Sun
    @email: autosunkai@gmail.com
    @date: 2021/8/5 15:52
    @updated: 2021/8/5 15:52
"""


def counting_sort(arr):
    if len(arr) < 2:
        return arr
    max_num = max(arr)
    count = [0 for _ in range(max_num + 1)]  # 开辟一个计数列表
    for a in arr:
        count[a] += 1
    arr.clear()
    for ind, val in enumerate(count):  # 提出计数序列的索引和值
        arr.extend([ind] * val)
    return arr
