#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
描述：合并K个排序链表,难度（hard）
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:
输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-k-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from Queue import PriorityQueue
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists) -> ListNode:
        """暴力法
        遍历所有链表，将所有节点的值放到一个数组中。
        将这个数组排序，然后遍历所有元素得到正确顺序的值。
        用遍历得到的值，创建一个新的有序链表
        时间复杂度 O（NlogN）
        空间复杂度 O（N）
        """
        res = []
        head = point = ListNode(0)
        while lists:
            node_list = lists.pop()
            while node_list:
                res.append(node_list.val)
                node_list = node_list.next
        for x in sorted(res):
            point.next = ListNode(x)
            point = point.next
        return head.next

    def mergeKLists2(self, lists) -> ListNode:
        """逐一两两合并链表
        将合并 k 个链表的问题转化成合并 2 个链表 k-1 次
        时间复杂度 O（kN） 其中 k 是链表的数目
        空间复杂度 O（1）
        """

        def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
            """双指针法"""
            head = ListNode(-1)
            p = head
            while l1 and l2:
                if l1.val < l2.val:
                    p.next = l1
                    l1 = l1.next
                else:
                    p.next = l2
                    l2 = l2.next
                p = p.next
            if l1:
                p.next = l1
            if l2:
                p.next = l2
            return head.next

        k = len(lists)
        if k == 0:
            return
        res = lists[0]
        for i in range(1, k):
            if lists[i]:
                res = mergeTwoLists(res, lists[i])
        return res

    def mergeKLists3(self, lists) -> ListNode:
        """使用优先队列
        时间复杂度 O（Nlogk） 其中 k 是链表的数目
        空间复杂度 O（N）
        """
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next