#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
描述：最小路径和 （难度：中等）
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def minPathSum(self, grid) -> int:
        """动态规划，时间和空间复杂度为O(m*n),二维数组"""
        if len(grid) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        # initial dp[][]
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1,m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1,n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[m - 1][n - 1]

    def minPathSum2(self, grid):
        """优化动态规划，时间复杂度为O(m*n), 空间复杂度为0(n), 一维数组"""
        if len(grid) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        dp = [0 for _ in range(n)]
        dp[0] = grid[0][0]
        for i in range(1, n):
            dp[i] = dp[i - 1] + grid[0][i]
        for i in range(1, m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = min(dp[j - 1], dp[j]) + grid[i][j]

        return dp[-1]

if __name__=="__main__":
    ss = Solution()
    test = [
        [1, 3, 1, 2],
        [1, 5, 1, 5],
        [4, 2, 1, 2],
        [2, 3, 1, 5]
    ]
    test2 = [
        [1, 3, 4, 8],
        [3, 2, 2, 4],
        [5, 7, 1, 9],
        [2, 3, 2, 3]
    ]
    print(ss.minPathSum(test2))
    print(ss.minPathSum2(test2))