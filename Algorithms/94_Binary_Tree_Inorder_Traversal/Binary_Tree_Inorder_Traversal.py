#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
描述：二叉树的中序遍历，难度（medium）
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode):
        """递归法"""
        result = []
        def helper(node):
            if not node:
                return
            helper(node.left)
            result.append(node.val)
            helper(node.right)
        helper(root)
        return result

    def inorderTraversal_2(self, root: TreeNode):
        """迭代法：栈"""
        result = []
        if not root:
            return result
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result.append(node.val)
            node = node.right
        return result


