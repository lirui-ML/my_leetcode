#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

描述：路径总和
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例: 
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def hasPathSum(self, root: TreeNode, target: int) -> bool:
        # 递归1
        if root is None:
            return False
        result = []
        self.add_node(result, root, target)
        return any(result)
        
    def add_node(self, result, node, target):
        if node:
            if not node.left and not node.right:
                if node.val == target:
                    result.append(True)
            if node.left:
                self.add_node(result, node.left, target - node.val)
            if node.right:
                self.add_node(result, node.right, target - node.val)
    
    def hasPathSum2(self, root: TreeNode, target: int) -> bool:
        if not root:
            return False
        target -= root.val
        if not root.left and not root.right:
            return target == 0
        return self.hasPathSum2(root.left, target) or self.hasPathSum2(root.right, target)
    
                
class Solution2:
    def hasPathSum(self, root: TreeNode, target: int) -> bool:
        # 递归-我的解法
        if root is None:
            return False
        self.res = []
        self.add_node(0, root, target)
        return any(self.res)
        
    def add_node(self, result, node, target):
        if node:
            result = node.val + result
            if not node.left and not node.right:
                if result == target:
                    self.res.append(1)
            if node.left:
                self.add_node(result, node.left, target)
            if node.right:
                self.add_node(result, node.right, target)
                
    def hasPathSum2(self, root: TreeNode, target: int) -> bool:
        # 迭代-使用栈进行深度优先搜索
        if root is None:
            return False
        stack = [(root, root.val)]
        while stack:
            node, curr_sum = stack.pop()
            if not node.left and not node.right and curr_sum == target:
                return True
            if node.left:
                stack.append((node.left, curr_sum + node.left.val))
            if node.right:
                stack.append((node.right, curr_sum + node.right.val))
        return False
        
        
        
        
        
        
                
                
        