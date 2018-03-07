#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Question:
	Given two binary strings, return their sum (also a binary string).

Example:
	a = "11"
	b = "1"
	Return "100".

'''

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2))[2:]    #bin()函数返回一个二进制数据，且前两位为0b,所以取[2:]