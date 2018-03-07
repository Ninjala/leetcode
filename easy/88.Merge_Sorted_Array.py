#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Question:
	Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
	You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. 
	The number of elements initialized in nums1 and nums2 are m and n respectively.

'''

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while n > 0:
            if nums1[m - 1] <= nums2[n - 1] or m <= 0:       #若nums1[m-1]比nums2[n-1]小(<=)或者m<=0(此时直接将nums2插入后面),将nums2[n-1]插入到nums1的后面
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1                 #因为nums2中一个元素已经插入到nums1中，所以令n-1
            else:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1