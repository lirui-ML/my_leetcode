#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
描述：寻找旋转排序数组中的最小值（难度：medium）
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

你可以假设数组中不存在重复元素。

示例 1:

输入: [3,4,5,1,2]
输出: 1
示例 2:

输入: [4,5,6,7,0,1,2]
输出: 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        """暴力搜索，时间复杂度O（n）"""
        min_num = nums[0]
        for i in nums:
            if i < min_num:
                min_num = i
        return min_num

    def findMin_2(self, nums: List[int]) -> int:
        """二分查找"""
        if len(nums) == 1:
            return nums[0]

        left, right = 0, len(nums) - 1
        if nums[right] > nums[0]:
            return nums[0]

        while left < right:
            mid = (right + left) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]

            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1

if __name__ == '__main__':
    testcase = [4, 5, 6, 7, 0, 1, 2]
    s = Solution()
    print(s.findMin_2(testcase))