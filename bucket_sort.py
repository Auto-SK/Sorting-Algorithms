# -*- coding: utf-8 -*-

"""
    @project: Sorting-Algorithms
    @version: v1.0.0
    @file: bucket_sort.py
    @brief: Bucket Sort
    @software: PyCharm
    @author: Kai Sun
    @email: autosunkai@gmail.com
    @date: 2021/8/5 14:15
    @updated: 2021/8/5 14:15
"""


def bucket_sort(arr):
    min_val = min(arr)
    max_val = max(arr)
    res = []

    # 桶的初始化
    bucket_size = 5  # 桶的大小
    bucket_count = (max_val - min_val) // bucket_size + 1  # 桶的数量
    buckets = [[] for _ in range(bucket_count)]

    # 利用映射函数将数据分配到每个桶中
    for a in arr:
        i = (a - min_val) // bucket_size
        buckets[i].append(a)
    for bucket in buckets:
        bucket.sort()
    for bucket in buckets:
        res.extend(bucket)  # 从 list 中提取
    return res
