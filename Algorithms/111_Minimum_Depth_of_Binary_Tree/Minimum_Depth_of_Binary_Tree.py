# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 14:36:58 2019

@author: HP
"""

"""
描述：
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

返回它的最小深度  2.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
         
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # 递归法 DFS 分而治之思想 时间复杂度 O(n)
        if root is None:
            return 0
        if root.left is None:
            return self.minDepth(root.right) + 1
        if root.right is None:
            return self.minDepth(root.left) + 1
        
        min_left = self.minDepth(root.left)
        min_right = self.minDepth(root.right)
        
        return min(min_left, min_right) + 1
        
    def minDepth_2(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left == None and root.right == None:
            return 1
        
        left = self.minDepth_2(root.left)
        right = self.minDepth_2(root.right)
        
        if root.left == None or root.right == None:
            return left + right + 1
        
        return min(left, right) + 1
        
         
