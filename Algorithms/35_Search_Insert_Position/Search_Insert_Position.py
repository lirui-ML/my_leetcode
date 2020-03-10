#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
描述：搜索插入位置，难度（easy）
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1
示例 3:

输入: [1,3,5,6], 7
输出: 4
示例 4:

输入: [1,3,5,6], 0
输出: 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-insert-position
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def searchInsert(self, nums, target: int) -> int:
        """暴力求解，O（n）时间复杂度"""
        if nums[0] > target:
            return 0
        elif nums[-1] < target:
            return len(nums)
        for idx, n in enumerate(nums):
            if n == target:
                return idx
            elif n < target < nums[idx + 1]:
                return idx + 1

    def searchInsert_2(self, nums, target: int) -> int:
        """二分查找法，O（logn）时间复杂度"""
        # if nums[0] > target:
        #     return 0
        # elif nums[-1] < target:
        #     return len(nums)
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

if __name__ == '__main__':
    test = [1, 3, 5, 6]
    target = 0
    st = Solution()
    print(st.searchInsert_2(test, target))