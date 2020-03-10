#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
描述：单词搜索，难度（medium）
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true.
给定 word = "SEE", 返回 true.
给定 word = "ABCB", 返回 false.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-search
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    # 定义上下左右四个行走方向
    directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def exist(self, board, word: str) -> bool:
        if board is None or len(board) == 0:
            return False
        self.M = len(board)
        self.N = len(board[0])

        mark = [[0 for _ in range(self.N)] for _ in range(self.M)]
        for i in range(self.M):
            for j in range(self.N):
                if board[i][j] == word[0]:
                    mark[i][j] = 1
                    if self.backtrack(i, j, mark, board, word[1:]):
                        return True
                    else:
                        mark[i][j] = 0
        return False

    def backtrack(self, i, j, mark, board, word):
        if len(word) == 0:
            return True

        for direct in Solution.directs:
            curr_i = i + direct[0]
            curr_j = j + direct[1]
            if curr_i >= 0 and curr_i < self.M and curr_j >= 0 and curr_j < self.N \
                and board[curr_i][curr_j] == word[0]:
                if mark[curr_i][curr_j] == 1:
                    continue
                mark[curr_i][curr_j] = 1
                if self.backtrack(curr_i, curr_j, mark, board, word[1:]):
                    return True
                else:
                    mark[curr_i][curr_j] = 0
        return False


if __name__=='__main__':
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word1 = 'ABCCED'
    word2 = 'SEE'
    word3 = 'ABCB'
    st = Solution()
    print(st.exist(board, word1))
    print(st.exist(board, word2))
    print(st.exist(board, word3))