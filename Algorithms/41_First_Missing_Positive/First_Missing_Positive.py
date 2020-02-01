#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
描述：缺失的第一个正数，难度（hard）
给定一个未排序的整数数组，找出其中没有出现的最小的正整数。

示例 1:
输入: [1,2,0]
输出: 3

示例 2:
输入: [3,4,-1,1]
输出: 2

示例 3:
输入: [7,8,9,11,12]
输出: 1

说明:
你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/first-missing-positive
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def firstMissingPositive(self, nums) -> int:
        """时间复杂度为O（n）的解法，空间复杂度为0(n)的解法"""
        size = len(nums)
        count = set()
        for i in nums:
            count.add(i)
        for i in range(1, size + 1):
            if i not in count:
                return i
        return size + 1

    def firstMissingPositive2(self, nums) -> int:
        """正确解法"""
        size = len(nums)
        for i in range(size):
            # 先判断这个数字是不是索引，然后判断这个数字是不是放在了正确的地方
            while 1 <= nums[i] <= size and nums[i] != nums[nums[i] - 1]:
                self._swap(nums, i, nums[i] - 1)
        for i in range(size):
            if i + 1 != nums[i]:
                return i + 1
        return size + 1

    def _swap(self, nums, index1, index2):
        nums[index1], nums[index2] = nums[index2], nums[index1]

if __name__=="__main__":
    test1 = [1,2,0]
    test2 = [3,4,-1,1]
    test3 = [7,8,9,11,12]
    sol = Solution()
    print(sol.firstMissingPositive(test1))
    print(sol.firstMissingPositive(test2))
    print(sol.firstMissingPositive(test3))