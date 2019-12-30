#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
描述：对称二叉树
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 递归
        if root is None:
            return True
        else:
            return self.isMirror(root.left, root.right)
            
    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        
        if left.val == right.val:
            return all([self.isMirror(left.left, right.right), 
                        self.isMirror(left.right, right.left)])
        else:
            return False
        
    def isSymmetric_2(self, root: TreeNode) -> bool:
        # 迭代
        if root is None:
            return True
        stack = [(root.left, root.right)]
        while len(stack) > 0:
            pair = stack.pop(0)
            left = pair[0]
            right = pair[1]
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val == right.val:
                stack.insert(0, [left.left, right.right])
                stack.insert(0, [left.right, right.left])
            else:
                return False
        return True
        
            
        