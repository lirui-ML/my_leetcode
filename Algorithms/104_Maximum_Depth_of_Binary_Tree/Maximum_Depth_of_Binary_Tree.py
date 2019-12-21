# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 16:40:57 2019

@author: HP
"""
"""
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点

示例：
给定二叉树 [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7
   
返回它的最大深度 3 
"""

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
        
class Solution:
    def maxDepth(self, root):
        # DFS 深度优先搜索, 采用递归写法，分而治之，时间复杂度 O(n)
        # 边界条件判断
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    def maxDepth_2(self, root):
        # 另一种 DFS 深度优先搜索的递归写法，时间复杂度 O(n)
        if root is None:
            return 0
        else:
            left = self.maxDepth_2(root.left)
            right = self.maxDepth_2(root.right)
        
        return max(left, right) + 1
    
    def maxDepth_3(self, root):
        # BFS 迭代法 和栈一起使用
        if not root:
            return 0
        
        stack = []
        if root is not None:
            stack.append((1, root))
        
        depth = 0
        while stack != []:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))
        
        return depth
            