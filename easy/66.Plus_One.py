#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Question:
	Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

	You may assume the integer do not contain any leading zero, except the number 0 itself.

	The digits are stored such that the most significant digit is at the head of the list.

'''

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for i in range(len(digits)):
        	num += digits[i] * pow(10, len(digits) - i -1)

        return [int(i) for i in str(num+1)]        #int类型不能迭代，所以先转换为str