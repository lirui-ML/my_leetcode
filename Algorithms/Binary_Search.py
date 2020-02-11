#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def binary_search(nums, target):
    """二分查找"""
    if len(nums) == 0:
        raise ValueError
    n = len(nums)
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

test = [-1, 3, 4, 6, 9, 15, 26, 30, 58]
target = 6
print(binary_search(test, target))