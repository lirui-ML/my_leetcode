#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
描述：最长上升子序列，难度（medium）
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:
输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。

说明:
可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def lengthOfLIS(self, nums) -> int:
        """暴力求解法"""
        pass

    def lengthOfLIS_2(self, nums) -> int:
        """动态规划，时间复杂度为O（N^2）"""
        if not nums:
            return 0
        n = len(nums)
        # 定义dp数组的含义，dp[n]表示第n个下标结尾的数组的最长上升子序列的长度
        dp = [1 for _ in range(n)]
        # 状态转移方程
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        print(dp)
        return max(dp)

    def lengthOfLIS_3(self, nums) -> int:
        """O（NlogN）解法"""
        # https://leetcode.com/problems/longest-increasing-subsequence/discuss/152065/Python-explain-the-O(nlogn)-solution-step-by-step


if __name__=="__main__":
    test = [10, 9, 2, 5, 3, 7, 101, 18]
    ss = Solution()
    print(ss.lengthOfLIS_2(test))
