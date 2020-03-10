#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
描述：路径总和 III，难度（easy）
给定一个二叉树，它的每个结点都存放着一个整数值。

找出路径和等于给定数值的路径总数。

路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

示例：
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

返回 3。和等于 8 的路径有:

1.  5 -> 3
2.  5 -> 2 -> 1
3.  -3 -> 11

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, target: int) -> int:
        """暴力求解,遍历所有节点，和所有路径"""
        # define global return val
        self.numOfPaths = 0
        # 1st layer DFS to go through each node
        self._helper(root, target)
        # return result
        return self.numOfPaths

    # define: traverse through the tree, at each treenode, call another DFS to test if a path sum include the answer
    def _helper(self, node: TreeNode, number: int):
        # exit condition
        if node is None:
            return
        # dfs break down
        self._judge(node, number)
        self._helper(node.left, number)
        self._helper(node.right, number)

    def _judge(self, node: TreeNode, number: int):
        if node is None:
            return
        if node.val == number:
            self.numOfPaths += 1
        self._judge(node.left, number - node.val)
        self._judge(node.right, number - node.val)

    def pathSum_2(self, root: TreeNode, target: int) -> int:
        """对暴力求解的优化，以空间换时间"""
        self.result = 0
        cache = {0 : 1}
        self.dfs(root, target, 0, cache)

        return self.result

    def dfs(self, root, target, currPathSum, cache):
        if root is None:
            return
        currPathSum += root.val
        oldPathSum = currPathSum - target
        self.result += cache.get(oldPathSum, 0)

        cache[currPathSum] = cache.get(currPathSum, 0) + 1

        self.dfs(root.left, target, currPathSum, cache)
        self.dfs(root.right, target, currPathSum, cache)
        cache[currPathSum] -= 1