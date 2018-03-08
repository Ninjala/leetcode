#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Question:
	Given two binary trees, write a function to check if they are the same or not.

	Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

	Input:     1         1
	          / \       / \
	         2   3     2   3

	        [1,2,3],   [1,2,3]

	Output: true

Example 2:

	Input:     1         1
	          /           \
	         2             2

	        [1,2],     [1,null,2]

	Output: false

Example 3:

	Input:     1         1
	          / \       / \
	         2   1     1   2

	        [1,2,1],   [1,1,2]

	Output: false

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:        #p和q都存在
        	return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q        #is比较p和q的地址是否相等，即是不是指向同一个内存单元