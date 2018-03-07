#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Question:
	The count-and-say sequence is the sequence of integers with the first five terms as following:

		1.     1
		2.     11
		3.     21
		4.     1211
		5.     111221
	1 is read off as "one 1" or 11.
	11 is read off as "two 1s" or 21.
	21 is read off as "one 2, then one 1" or 1211.
	Given an integer n, generate the nth term of the count-and-say sequence.

	Note: Each term of the sequence of integers will be represented as a string.

Example 1:

	Input: 1
	Output: "1"

Example 2:

	Input: 4
	Output: "1211"

'''

import re

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'          # s为第一项的值（设成字符串型，是为了便于进行字符串加减）
        for _ in range(n - 1):
            s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
        return s

 # '(.)\1*'中，'\1'表示重复匹配第一个括号中的内容。 
 # re.sub()函数用于替换字符串中的匹配项,即将s中匹配的值替换为lambda m返回的值
