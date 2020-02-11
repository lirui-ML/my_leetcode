#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
描述：翻转二叉树，难度（easy）
翻转一棵二叉树。

示例：

输入：
     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：
     4
   /   \
  7     2
 / \   / \
9   6 3   1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/invert-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """递归"""
        def helper(node):
            if node is None:
                return
            if node.left is None and node.right is None:
                return
            if node.left:
                tmp = node.left
                node.left = node.right
                node.right = tmp
            elif node.right:
                tmp = node.right
                node.right = node.left
                node.left = tmp
            helper(node.left)
            helper(node.right)
        helper(root)
        return root

    def invertTree_2(self, root: TreeNode) -> TreeNode:
        """迭代"""
        if root is None:
            return
        stack = [root]
        while stack:
            curr = stack.pop()
            tmp = curr.left
            curr.left = curr.right
            curr.right = tmp
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return root