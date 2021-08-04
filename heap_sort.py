# -*- coding: utf-8 -*-

"""
    @project: Sorting-Algorithms
    @version: v1.0.0
    @file: heap_sort.py
    @brief: Heap Sort
    @software: PyCharm
    @author: Kai Sun
    @email: autosunkai@gmail.com
    @date: 2021/8/4 20:42
    @updated: 2021/8/4 20:42
"""


def build_heap(arr):
    for i in range(len(arr) // 2 - 1,  -1, -1):     # 从 n / 2 - 1 到 0 开始建堆
        heapify(arr, len(arr), i)


def heapify(arr, n, i):
    """
    :param arr: 要建堆的数组
    :param n: 堆的长度
    :param i: 要入堆的元素的索引
    :return: None
    """
    left = 2 * i + 1    # 左子节点
    right = 2 * i + 2   # 右子节点
    largest = i
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    build_heap(arr)
    for l in range(len(arr) - 1, 0, -1):    # 从 n - 1 到 1 重复堆化
        arr[0], arr[l] = arr[l], arr[0]
        heapify(arr, l, 0)
    return arr
