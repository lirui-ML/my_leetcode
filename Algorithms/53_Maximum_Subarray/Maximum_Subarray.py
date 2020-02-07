#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
描述：最大子序和，难度（easy）
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def maxSubArray(self, nums) -> int:
        """暴力求解，O（N^2）时间复杂度"""
        if not nums:
            return 0
        n = len(nums)
        res = nums[0]
        for i in range(n):
            tmp = 0
            for j in range(i, n):
                tmp += nums[j]
                if tmp > res:
                    res = tmp
        return res

    def maxSubArray_2(self, nums) -> int:
        """动态规划，O（N）时间复杂度"""
        if not nums:
            return 0
        n = len(nums)
        # dp数组 表示以i结尾的数组的最大子序和
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)

    def maxSubArray_2(self, nums) -> int:
        if len(nums) == 0:
            return 0
        n = len(nums)
        dp = [0 for i in range(n)]
        dp[0] = nums[0]
        result = dp[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1], 0) + nums[i]
            result = max(dp[i], result)
        return result

if __name__=="__main__":
    test = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    test1 = [0, 1, -1]
    ss = Solution()
    print(ss.maxSubArray_2(test))
