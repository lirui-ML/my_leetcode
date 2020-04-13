#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
二叉树的层次遍历 II（难度：easy）
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            level_size = len(queue)
            current_leval = []
            for _ in range(level_size):
                node = queue.popleft()
                current_leval.append(node.val)
                if node.left:
                    queue.append(node.left)
                if  node.right:
                    queue.append(node.right)
            res.append(current_leval)
        return res[::-1]
