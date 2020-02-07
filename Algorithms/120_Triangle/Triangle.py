#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
描述：三角形最小路径和，难度（medium）
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

说明：
如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/triangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def minimumTotal(self, triangle) -> int:
        """动态规划，自底向上，时间复杂度为O(N*2),空间复杂度为O(m*n)"""
        if len(triangle) == 0:
            return 0
        elif len(triangle) == 1:
            return triangle[0][0]
        n = len(triangle)
        dp = triangle[-1]

        for level in range(n - 2, -1, -1):
            for i in range(len(triangle[level])):
                dp[i] = min(dp[i], dp[i + 1]) + triangle[level][i]
        return dp[0]

    def minimumTotal_2(self, triangle) -> int:
        "动态规划，自顶向下, 空间复杂度为O(1)"
        if not triangle:
            return 0
        n = len(triangle)
        if n == 1:
            return triangle[0][0]
        for i in range(1, n):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] = triangle[i - 1][j] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    triangle[i][j] = triangle[i - 1][j - 1] + triangle[i][j]
                else:
                    triangle[i][j] = min(triangle[i - 1][j - 1], triangle[i - 1][j]) + triangle[i][j]
        return min(triangle[-1])


if __name__=="__main__":
    sample = [
        [2],
       [3,4],
      [6,5,7],
     [4,1,8,3]
    ]
    ss = Solution()
    print(ss.minimumTotal(sample))
    print(ss.minimumTotal_2(sample))


