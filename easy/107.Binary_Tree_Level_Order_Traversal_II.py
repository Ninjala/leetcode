#!/usr/bin/env python
# -*- coding： utf-8 -*-

'''
Question:
	Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

Example:
	Given binary tree [3,9,20,null,null,15,7],
	    3
	   / \
	  9  20
	    /  \
	   15   7
	return its bottom-up level order traversal as:
	[
	  [15,7],
	  [9,20],
	  [3]
	]

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        stack = [(root, 0)]
        res = []
        while stack:                 #栈不为空时
            node, level = stack.pop()           
            if node:                #节点存在时
                if len(res) < level+1:             #判断节点是否在同一层，若不是，添加[]
                    res.append([])
                res[level].append(node.val)
                stack.append((node.right, level+1))
                stack.append((node.left, level+1))
        return res[::-1]                  #将结果反转