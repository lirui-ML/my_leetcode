#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
描述：寻找峰值（难度：medium）
峰值元素是指其值大于左右相邻值的元素。

给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。

数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞。

示例 1:

输入: nums = [1,2,3,1]
输出: 2
解释: 3 是峰值元素，你的函数应该返回其索引 2。
示例 2:

输入: nums = [1,2,1,3,5,6,4]
输出: 1 或 5
解释: 你的函数可以返回索引 1，其峰值元素为 2；
     或者返回索引 5， 其峰值元素为 6。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-peak-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """常规解法，O（n）时间复杂度"""
        # 特殊情况下判断
        if len(nums) <= 1:
            return 0
        for i in range(len(nums)):
            if i == 0:
                if nums[i] > nums[i + 1]:
                    return i
            elif i == len(nums) - 1:
                if nums[i] > nums[i - 1]:
                    return i
            else:
                if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                    return i
        return -1

    def findPeakElement_2(self, nums: List[int]) -> int:
        """时间复杂度为O（logn）的解法"""
        if len(nums) == 1:
            return 0
        elif len(nums) < 1:
            return -1
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] > nums[mid - 1] and nums[mid] < nums[mid + 1]:
                start = mid
            else:
                end = mid
        if nums[start] > nums[end]:
            return start

        return end


if __name__ == '__main__':
    tesecase1 = [1, 2, 3, 1]
    tesecase2 = [1,2,1,3,5,6,4]
    s = Solution()
    print(s.findPeakElement(tesecase1))
    print(s.findPeakElement(tesecase2))