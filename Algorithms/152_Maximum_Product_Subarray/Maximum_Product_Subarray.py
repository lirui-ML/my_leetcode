#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
描述：乘积最大子序列，难度（medium）
给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。

示例 1:
输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。

示例 2:
输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def maxProduct(self, nums) -> int:
        """暴力法，时间复杂度为O(N*2)，空间复杂度为O(1)"""
        if not nums:
            return 0
        result = nums[0]
        for i in range(len(nums)):
            tmp = 1
            for j in range(i, len(nums)):
                tmp *= nums[j]
                if tmp > result:
                    result = tmp
        return result

    def maxProduct_2(self, nums) -> int:
        """动态规划，时间复杂度为 O(N),空间复杂度为 O(N)"""
        if not nums:
            return 0
        n = len(nums)
        dpmax, dpmin, res = [0 for _ in range(n)], [0 for _ in range(n)], nums[0]
        dpmax[0], dpmin[0] = nums[0], nums[0]
        for i in range(1, len(nums)):
            dpmax[i] = max(max(dpmax[i - 1] * nums[i], nums[i]), dpmin[i - 1] * nums[i])
            dpmin[i] = min(min(dpmax[i - 1] * nums[i], nums[i]), dpmin[i - 1] * nums[i])
            res = max(res, dpmax[i])
        return res



if __name__=="__main__":
    sample = [2, 3, -2, 4]
    sample2 = [-2, 0, -1]
    sample3 = [0, 2]
    ss = Solution()
    print(ss.maxProduct_2(sample))
    print(ss.maxProduct_2(sample2))
    print(ss.maxProduct_2(sample3))