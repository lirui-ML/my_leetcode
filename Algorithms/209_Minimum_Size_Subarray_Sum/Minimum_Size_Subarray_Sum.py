#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
描述： 长度最小的子数组（难度：medium）
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。

示例:

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
进阶:

如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
"""

from typing import List

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        """滑动窗口，O（n）时间复杂度"""
        min_length = len(nums)
        if sum(nums) < s:
            return 0

        left = 0
        right = 1
        while left < len(nums) and right <= len(nums):
            if sum(nums[left:right]) < s:
                right += 1
            else:
                min_length = min(min_length, right - left)
                left += 1
        return min_length

    def minSubArrayLen_2(self, s: int, nums: List[int]) -> int:
        """滑动窗口2"""
        total = left = 0
        min_length = len(nums) + 1
        for right in range(len(nums)):
            total += nums[right]
            while total >= s:
                min_length = min(min_length, right - left + 1)
                total -= nums[left]
                left += 1
        return 0 if min_length == len(nums) + 1 else min_length

    def minSubArrayLen_3(self,  s: int, nums: List[int]) -> int:
        """"""
        pass
if __name__ == '__main__':
    test = [2,3,1,2,4,3]
    print(test[5:6])
    s = Solution()
    print(s.minSubArrayLen(7, test))