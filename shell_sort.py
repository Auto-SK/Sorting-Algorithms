# -*- coding: utf-8 -*-

"""
    @project: Sorting-Algorithms
    @version: v1.0.0
    @file: shell_sort.py
    @brief: Shell Sort
    @software: PyCharm
    @author: Kai Sun
    @email: autosunkai@gmail.com
    @date: 2021/8/3 18:03
    @updated: 2021/8/3 18:03
"""


def insertion_sort_gap(arr, gap):           # 将 gap 看作隔 gap 个距离摸一张牌，而不是依次按顺序摸牌
    for i in range(gap, len(arr)):          # 将 i 看作摸到的牌的下标
        value = arr[i]                      # 将摸到的牌存储到 value
        j = i - gap                         # 将 j 看作手里的牌的下标
        while j >= 0 and arr[j] > value:    # 如果手里的牌大于摸到的牌
            arr[j + gap] = arr[j]           # 将手里的牌右移 gap 个距离
            j -= gap                        # 下标 j 左移 gap 个距离
        arr[j + gap] = value                # 将摸到的牌插入到 j + gap 位置


def shell_sort_part(arr):                   # 分开写 shell 排序
    d = len(arr) // 2                       # 第一次分组
    while d >= 1:
        insertion_sort_gap(arr, d)          # 调用插入排序
        d //= 2                             # 整除 2 后再次分组
    return arr


def shell_sort(arr):                        # 合到一起
    gap = len(arr) // 2                     # 第一次分组
    while gap >= 1:                         # 将 gap 看作隔 gap 个距离摸一张牌，而不是依次顺序摸牌
        for i in range(gap, len(arr)):      # 将 i 看作摸到的牌的下标
            value = arr[i]                  # 将摸到的牌存储到 value
            j = i - gap                     # 将 j 看作手里的牌的下标
            while j >= 0 and arr[j] > value:
                arr[j + gap] = arr[j]       # 将手里的牌右移 gap 个距离
                j -= gap                    # 下标 j 左移 gap 个距离
            arr[j + gap] = value            # 将摸到的怕插入到 j + gap 位置
        gap //= 2                           # 整除 2 后再分组
    return arr

