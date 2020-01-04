#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
描述：路径总和 II
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, target: int):
        # 递归
        self.result = []
        if not root:
            return self.result
        init_path = []
        self.add_node(target, root, init_path)
        
        return self.result
    
    def add_node(self, target, node, path):
        if node:
            # 需要注意path的传递
            if not node.left and not node.right:
                if sum(path + node.val) == target:
                    path.append(node.val)
                    self.result.append(path)
            if node.right:
                self.add_node(target, node.right, path + [node.val])
            if node.left:
                self.add_node(target, node.left, path + [node.val])
                
    def pathSum2(self, root: TreeNode, target: int):
        # 递归
        if not root:
            return []
        if not root.left and not root.right and target == root.val:
            return [[root.val]]
        tmp = self.pathSum(root.left, target - root.val) + self.pathSum(root.right, target - root.val)
        return [[root.val]+i for i in tmp]
        
    
    def pathSum3(self, root: TreeNode, target: int):
        # BFS + queue
        if not root:
            return []
        res = []
        queue = [(root, root.val, [root.val])]
        while queue:
            curr, val, ls = queue.pop(0)
            if not curr.left and not curr.right and val == target:
                res.append(ls)
            if curr.left:
                queue.append((curr.left, val+curr.left.val, ls+[curr.left.val]))
            if curr.right:
                queue.append((curr.right, val+curr.right.val, ls+[curr.right.val]))
        return res
    
    def pathSum4(self, root: TreeNode, target: int):
        # DFS + stack I
        if not root:
            return []
        result = []
        stack = [(root, [root.val])]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right and sum(path) == target:
                result.append(path)
            if node.right:
                stack.append((node.right, path + [node.right.val]))
            if node.left:
                stack.append((node.left, path + [node.left.val]))
        return result
       
    def pathSum5(self, root: TreeNode, target: int):
        # DFS + stack II
        if not root:
            return []
        result = []
        stack = [(root, target - root.val, [root.val])]
        while stack:
            curr, val, ls = stack.pop()
            if not curr.left and not curr.right and val == 0:
                result.append(ls)
            if curr.right:
                stack.append((curr.right, val - curr.right.val, ls + [curr.right.val]))
            if curr.left:
                stack.append((curr.left, val - curr.left.val, ls + [curr.left.val]))
                
        return result
        