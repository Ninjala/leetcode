#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Question:
	Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

	Input: 123
	Output:  321
Example 2:

	Input: -123
	Output: -321
Example 3:

	Input: 120
	Output: 21

'''

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = (x > 0) - (x < 0)                      #若x > 0,则s = 1,若x < 0,则s = -1
        r = int(str(x*s)[::-1])
        return r*s if r < 2**31-1 else 0