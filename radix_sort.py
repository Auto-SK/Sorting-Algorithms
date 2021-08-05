# -*- coding: utf-8 -*-

"""
    @project: Sorting-Algorithms
    @version: v1.0.0
    @file: radix_sort.py
    @brief: Radix Sort
    @software: PyCharm
    @author: Kai Sun
    @email: autosunkai@gmail.com
    @date: 2021/8/5 21:18
    @updated: 2021/8/5 21:18
"""


def radix_sort(arr):
    digit = 0       # 当前位数
    max_digit = 1   # 最大位数
    max_value = max(arr)

    # 找出序列中最大的位数
    while 10 ** max_digit < max_value:
        max_digit += 1

    while digit < max_digit:
        count = [[] for _ in range(10)]  # 开辟一个计数列表
        for a in arr:
            d = (a // 10 ** digit) % 10  # 求出 digit 位对应的值
            count[d].append(a)
        # 计数排序
        arr.clear()
        for c in count:
            arr.extend(c)
        digit += 1
    return arr
