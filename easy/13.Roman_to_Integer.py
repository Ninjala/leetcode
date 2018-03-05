#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Question:
	Given a roman numeral, convert it to an integer.

	Input is guaranteed to be within the range from 1 to 3999.

Tips:
	I - 1
	V - 5
	X - 10
	L - 50
	C - 100
	D - 500
	M - 1000

	1.相同的数字连写，所表示的数等于这些数字相加得到的数，例如：III = 3
	2.小的数字在大的数字右边，所表示的数等于这些数字相加得到的数，例如：VIII = 8
	3.小的数字，限于（I、X和C）在大的数字左边，所表示的数等于大数减去小数所得的数，例如：IV = 4
	4.正常使用时，连续的数字重复不得超过三次
	5.在一个数的上面画横线，表示这个数扩大1000倍（本题只考虑3999以内的数，所以用不到这条规则）

'''

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
	    roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
	    z = 0
	    for i in range(len(s)-1):
	    	if roman_dict[s[i]] < roman_dict[s[i+1]]:      #小的数字在大的数字左边
	    		z -= roman_dict[s[i]]
	    	else:
	    		z +=  roman_dict[s[i]]
	    return z + roman_dict[s[-1]]



