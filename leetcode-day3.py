# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 14:57:21 2019

@author: 刘瑞
"""
"""
题目描述：
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
思路：只要把数组中所有的非零元素，按顺序给数组的前段元素位赋值，剩下的全部直接赋值 0
"""
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count=nums.count(0)
        nums[:]=[i for i in nums if i != 0]
        nums+=[0]*count  
        return nums
        
"""        
讨论区看到的一行解法
def moveZeroes(self, nums):
	nums.sort(key=lambda x: x == 0)
"""
nums=[1,2,3,0,5,0,0,6,0,7]
test=Solution()
test.moveZeroes(nums)
print(nums)