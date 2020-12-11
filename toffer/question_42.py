#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
剑指 Offer 42. 连续子数组的最大和
输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。

示例1:

输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        n = len(nums)
        # 定义dp，dp[i]代表以元素nums[i]为结尾的连续子数组最大和，初始化dp
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        # 
        for i in range(1, n):
            dp[i] = nums[i] + max(dp[i - 1], 0)
            
        return max(dp)

    def maxSubArray2(self, nums: List[int]) -> int:
        """动态规划，时间复杂度为O(n),空间复杂度O(1)"""
        if len(nums) == 0:
            return 0
        max_num = nums[0]
        former = 0
        curr = 0
        for i in nums:
            curr = i
            if former > 0:
                curr += former
            if curr > max_num:
                max_num = curr
            former = curr
        return max_num

if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    sol = Solution()
    sol.maxSubArray(nums)