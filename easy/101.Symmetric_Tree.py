#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Question:
	Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

Example:
	this binary tree [1,2,2,3,4,4,3] is symmetric:

	    1
	   / \
	  2   2
	 / \ / \
	3  4 4  3
	But the following [1,2,2,null,3,null,3] is not:
	    1
	   / \
	  2   2
	   \   \
	   3    3
Note:
	Bonus points if you could solve it both recursively and iteratively.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """        
        if root is None:
        	return True

        stack = [(root.left, root.right)]

        while stack:
        	left, right = stack.pop()
        	if left is None and right is None:        #若左节点与右节点都为空，则说明相等，跳出本次循环进行下一次，while判断stack为空，跳出循环，返回True
        		continue
        	if left is None or right is None:     #若左节点与右节点其中一个为空，则说明不对称
        		return False
        	if left.val == right.val:            #如果左节点与右节点的值相等，说明根下的两子节点对称，然后将左节点的左子节点与右节点的右子节点压入栈中（因为要判断是否对称）
        		stack.append((left.left, right.right))
        		stack.append((left.right, right.left))       #同理将左节点的右子节点与右节点的左子节点压入栈中，等待下次循环判断
        	else:
        		return False

        return True