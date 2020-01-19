#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
描述：不同路径 II （难度：中等）
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

网格中的障碍物和空位置分别用 1 和 0 来表示。

说明：m 和 n 的值均不超过 100。

示例 1:

输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2
解释:
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        """动态规划, 时间复杂度O(m*n), 空间复杂度O(m*n)"""
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        # 边界条件
        if m == 0 or n == 0:
            return 0
        if obstacleGrid[0][0] == 1:
            return 0
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1

        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1
        # 动态转移方程
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m -1][n - 1]

    def uniquePathsWithObstacles2(self, obstacleGrid) -> int:
        """动态规划优化, 使用ob数组，额外空间为O(1)"""
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if m == 0 or n == 0:
            return 0
        if obstacleGrid[0][0] == 1:
            return 0
        obstacleGrid[0][0] = 1
        for i in range(1,m):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i - 1][0] == 1)
        for j in range(1,n):
            obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j - 1] == 1)
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
                else:
                    obstacleGrid[i][j] = 0

        return obstacleGrid[m - 1][n - 1]

    def uniquePathsWithObstacles3(self, obstacleGrid) -> int:
        """动态规划优化, 额外空间为O(n)"""
        if not obstacleGrid:
            return
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n
        dp[0] = 1 - obstacleGrid[0][0]
        for i in range(1, n):
            dp[i] = dp[i - 1] * (1 - obstacleGrid[0][i])

        for i in range(1, m):
            dp[0] *= (1 - obstacleGrid[i][0])
            for j in range(1, n):
                dp[j] = (dp[j - 1] + dp[j]) * (1 - obstacleGrid[i][j])

        return dp[-1]

if __name__=="__main__":
    ss = Solution()
    a = [
        [0,0,0],
        [0,1,0],
        [0,0,0]
    ]
    b = [[0,1]]
    print(ss.uniquePathsWithObstacles(a))
    print(ss.uniquePathsWithObstacles3(a))