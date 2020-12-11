#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
剑指 Offer 47. 礼物的最大价值
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

示例 1:

输入: 
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
from pprint import pprint

class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        """动态规划，时间复杂度和空间复杂度均为0(n^2)"""
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        # 二维数组dp
        dp = [[0] * n for _ in range(m)]
        # 初始化dp
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        # dp状态转移方程
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = max([dp[i][j - 1], dp[i - 1][j]]) + grid[i][j]
        return dp[m - 1][n - 1]

    def maxValue2(self, grid: List[List[int]]) -> int:
        """动态规划，时间复杂度和空间复杂度均为0(n)"""
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        # 初始化dp
        dp = [0 for _ in range(n)]
        dp[0] = grid[0][0]
        for i in range(1, n):
            dp[i] = dp[i - 1] + grid[0][i]
        # dp状态转移方程
        for i in range(1, m):
            dp[0] = dp[0] + grid[i][0]
            for j in range(1, n):
                dp[j] = max([dp[j - 1], dp[j]]) + grid[i][j]
        return dp[-1]




if __name__ == "__main__":
    a = [[1,3,1],
        [1,5,1],
        [4,2,1]
        ]
    sol = Solution()
    sol.maxValue2(a)
