#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
描述：二叉树的前序遍历，难度（medium）
给定一个二叉树，返回它的 前序 遍历。

 示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,2,3]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-preorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode):
        """递归法"""
        result = []
        def helper(node):
            if not node:
                return
            result.append(node.val)
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)
        helper(root)
        return result

    def preorderTraversal_2(self, root: TreeNode):
        """迭代法：栈"""
        result = []
        if root is None:
            return result
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result


