# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 22:18:05 2019

@author: 刘瑞
"""
"""
题目描述： 三数之和
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

思路：思路为迭代nums中的每个数字，每次选择一个数字，然后用双指针遍历剩下的数字，找到两个数字使三个数字之和为零
首先对数组进行排序，之后根据和的情况向左或者向右移动指针，直到找到符合情况的数组
***注意如何跳过相同的数组，以及剔除一些不需要计算的情况和边界条件***
"""

class Solution(object):
	def threeSum(self, nums):
		res = []
		nums.sort()
		length = len(nums)
		for i in range(length-2): 
			if nums[i]>0: break 
			if i>0 and nums[i]==nums[i-1]: continue 

			l, r = i+1, length-1 
			while l<r:
				total = nums[i]+nums[l]+nums[r]

				if total<0: 
					l+=1
				elif total>0: 
					r-=1
				else: 
					res.append([nums[i], nums[l], nums[r]])
					while l<r and nums[l]==nums[l+1]: 
						l+=1
					while l<r and nums[r]==nums[r-1]: 
						r-=1
					l+=1
					r-=1
		return res