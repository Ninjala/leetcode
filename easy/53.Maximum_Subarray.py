#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Question:
	Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

Example:
	given the array [-2,1,-3,4,-1,2,1,-5,4],
	the contiguous subarray [4,-1,2,1] has the largest sum = 6.

'''

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
        	return 0

        cur_sum = max_sum = nums[0]             #当前和与最大和   
        for num in nums[1:]:
        	cur_sum = max(num, cur_sum + num)
        	max_sum = max(cur_sum, max_sum)

        return max_sum