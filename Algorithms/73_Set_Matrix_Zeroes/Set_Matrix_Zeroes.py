#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
描述：矩阵置0，难度（medium）
给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

示例 1:
输入:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
示例 2:
输入:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
输出:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
进阶:

一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
你能想出一个常数空间的解决方案吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/set-matrix-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import pprint

class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        O（m*n）时间复杂度，O（m+n）空间复杂度
        """
        if matrix is None or len(matrix) == 0:
            return
        m = len(matrix)
        n = len(matrix[0])

        zero_row = set()
        zero_col = set()
        # zero row and col
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_row.add(i)
                    zero_col.add(j)
        # set 0
        for i in range(m):
            for j in range(n):
                if i in zero_row or j in zero_col:
                    matrix[i][j] = 0

    def setZeroes(self, matrix):
        """设置虚拟值，O（1）的额外空间"""
        MODIFIED = -1000000
        R = len(matrix)
        C = len(matrix[0])
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    # We modify the elements in place. Note, we only change the non zeros to MODIFIED
                    for k in range(C):
                        matrix[r][k] = MODIFIED if matrix[r][k] != 0 else 0
                    for k in range(R):
                        matrix[k][c] = MODIFIED if matrix[k][c] != 0 else 0
        for r in range(R):
            for c in range(C):
                # Make a second pass and change all MODIFIED elements to 0 """
                if matrix[r][c] == MODIFIED:
                    matrix[r][c] = 0

if __name__=="__main__":
    test1 = [
        [1,1,1],
        [1,0,1],
        [1,1,1]
    ]
    test2 = [
        [0,1,2,0],
        [3,4,5,2],
        [1,3,1,5]
    ]

    st = Solution()
    st.setZeroes(test1)
    st.setZeroes(test2)
