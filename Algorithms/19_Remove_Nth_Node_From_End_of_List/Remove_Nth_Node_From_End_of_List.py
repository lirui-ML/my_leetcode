#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
描述：删除链表的倒数第N个节点 (难度：medium）
删除链表的倒数第N个节点
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 单次遍历，时间复杂度为O(n), 空间复杂度也是O(n)
        nodelist = []
        node = head
        while node:
            nodelist.append(node)
            node = node.next
        if n == len(nodelist):
            return head.next
        else:
            nodelist[-n - 1].next = nodelist[-n].next
            return head


    def removeNthFromEnd2(self, head: ListNode, n:int) -> ListNode:
        # 单次遍历,运用双指针,时间复杂度为 O(n), 空间复杂度 O(1)
        newhead = ListNode(0)
        newhead.next = head
        p, q = newhead, newhead
        for _ in range(n):
            q = q.next
        while q.next:
            q = q.next
            p = p.next
        p.next = p.next.next
        return  newhead.next

