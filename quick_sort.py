# -*- coding: utf-8 -*-

"""
    @project: Sorting-Algorithms
    @version: v1.0.0
    @file: quick_sort.py
    @brief: Quick Sort
    @software: PyCharm
    @author: Kai Sun
    @email: autosunkai@gmail.com
    @date: 2021/8/4 0:01
    @updated: 2021/8/4 0:01
"""


def quick_sort(arr):
    def quicksort(l, r):
        # 子数组长度为 1 时终止递归
        if l >= r:
            return
        # 哨兵划分操作（以 arr[l] 作为基准数）
        i, j = l, r
        while i < j:
            while i < j and arr[j] >= arr[l]:
                j -= 1
            while i < j and arr[i] <= arr[l]:
                i += 1
            arr[i], arr[j] = arr[j], arr[i]
        arr[l], arr[i] = arr[i], arr[l]
        # 递归左（右）子数组执行哨兵划分
        quicksort(l, i - 1)
        quicksort(i + 1, r)

    quicksort(0, len(arr) - 1)
    return arr
