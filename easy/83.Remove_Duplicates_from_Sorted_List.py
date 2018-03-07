#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Question:
	Given a sorted linked list, delete all duplicates such that each element appear only once.

Example:
	Given 1->1->2, return 1->2.
	Given 1->1->2->3->3, return 1->2->3.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur:
            while cur.next and cur.val == cur.next.val:
                cur.next = cur.next.next                 #当所指节点等于下个节点时，跳过下个节点，与后继节点相连接
            cur = cur.next          #若不相等，则移动到下一个节点
        return head