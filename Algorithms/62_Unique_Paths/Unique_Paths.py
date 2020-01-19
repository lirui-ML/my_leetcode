#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
描述：不同路径 (难度：中等）
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？


例如，上图是一个7 x 3 的网格。有多少可能的路径？

说明：m 和 n 的值均不超过 100。

示例 1:

输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右
示例 2:

输入: m = 7, n = 3
输出: 28

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """递归"""
        def path(x: int, y:int) -> int:
            if x == 0 or y == 0:
                return 1
            return path(x - 1, y) + path(x, y - 1)

        return path(m - 1, n - 1)

    def uniquePaths_2(self, m: int, n: int) -> int:
        """动态规划, 时间复杂度O(m*n), 空间复杂度O(m*n)"""
        if m == 0 or n == 0:
            return 0
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

    def uniquePaths_3(self, m: int, n: int) -> int:
        """优化动态规划, 通过画表可以将空间复杂度优化为O(n)"""
        if m == 0 or n == 0:
            return 0
        dp = [1 for _ in range(n)]
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j] + dp[j - 1]
        return dp[n - 1]

if __name__=="__main__":
    s = Solution()
    m, n = (6, 5)
    print(s.uniquePaths(m, n))
    print(s.uniquePaths_2(m, n))
    print(s.uniquePaths_3(m, n))