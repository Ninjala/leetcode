#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Question:
	Write a function to find the longest common prefix string amongst an array of strings.
	
'''

from functools import reduce

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        def lcp(s, t):
            if len(s)>len(t):
                s, t = t, s
            for i in range(len(s)):
                if s[i]!=t[i]:
                    return s[:i]
            return s
        return reduce(lcp,strs) if strs else ""