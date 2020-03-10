#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
描述：在排序数组中查找元素的第一个和最后一个位置，难度（medium）
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]

示例 2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def searchRange(self, nums, target: int):
        """时间复杂度为O（logn），二分法"""
        if len(nums) == 0:
            return [-1, -1]
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                tem_left, tem_right = mid, mid
                while tem_left >= 0 and nums[tem_left] == nums[mid]:
                    tem_left -= 1
                while tem_right < len(nums) and nums[tem_right] == nums[mid]:
                    tem_right += 1
                return [tem_left + 1, tem_right - 1]

            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return [-1, -1]

if __name__ == '__main__':
    test = [5, 7, 7, 8, 8, 10]
    target = 7
    st = Solution()
    print(st.searchRange([1], 1))