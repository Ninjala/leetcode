#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Question:
	Merge two sorted linked lists and return it as a new list. 

	The new list should be made by splicing together the nodes of the first two lists.

	将已经排好序的两个链表合并为一个链表，新的链表也必须是有序的。

Example:
	Input: 1->2->4, 1->3->4
	Output: 1->1->2->3->4->4

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def mergeTwoLists(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         if l1 and l2:
#             if l1.val > l2.val:
#                 l1, l2 = l2, l1
#             l1.next = self.mergeTwoLists(l1.next, l2)
#         return l1 or l2

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        mergelist = ListNode(0)           #先创建一个链表,指向0
        temp = mergelist                  #将链表赋给temp
        while l1 != None and l2 != None:        #当l1与l2不为空时，进入循环
            if l1.val < l2.val:                   
                temp.next = l1            #当l1小于l2时，将l1添加到temp的后面
                l1 = l1.next             #将l1指向l1的下一个
            else:
                temp.next = l2          #当l1大于l2时，将l2添加到temp的后面
                l2 = l2.next             #将l2指向l2的下一个
            temp = temp.next               #最后将temp向后移动，指向其最后一个（下一个）值
        if l1 != None:
            temp.next = l1
        else:
            temp.next = l2
        return mergelist.next