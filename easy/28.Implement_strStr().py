#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Question:
	Implement strStr().

	Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example1:
	Input: haystack = "hello", needle = "ll"
	Output: 2

Example2:
	Input: haystack = "aaaaa", needle = "bba"
	Output: -1

'''

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)         #之所以不用index()是因为若needle不在haystack中，会报错