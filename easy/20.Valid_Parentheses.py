#!/usr/bin/env python
# -*- coding: utf-8 -*-
#需要用到栈

'''
Question:
	Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

	The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

'''

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict = {')':'(', ']':'[', '}':'{'}
        for char in s:
        	if char in dict.values():           #若s中的char有与dict中的value匹配的话,将char压入stack中
        		stack.append(char)
        	elif char in dict.keys():           #若s中的char有与dict中的key匹配的话，再进行筛选
        		if stack == [] or dict[char] != stack.pop():            #若stack此时为空，或者与之前stack中存储的不同时（即不是一组括号），返回False
        			return False
        	else:
        		return False
        return stack == []                       #若括号都验证成功，则stack将为空，即stack == []结果为True