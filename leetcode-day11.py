# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 20:15:50 2019

@author: 刘瑞
"""
"""
题目描述：长度最小的子数组
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。

示例: 

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。


思路：采用滑动窗口的思路。定义两个指针，要求是连续子数组，所以我们必须定义 left，right两个指针，left 向前遍历，right向后遍历，
相当与一个滑块，这样所有的子数组都会在 [left...right] 中出现，如果 nums[left...right] 的和小于目标值 s，那么right向后移一位，再次比较，
直到大于目标值 s 之后，left 向前移动一位，缩小数组的长度。遍历到i到数组的最末端，就算结束了，如果不存在符合条件的就返回 0。
"""
class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left, right, Sum, result = 0, 0, 0, len(nums)+1
        while left < len(nums):
            if right < len(nums) and Sum < s:
                Sum = Sum + nums[right]
                right += 1
            else:
                Sum = Sum - nums[left]
                left += 1
            if Sum >= s:
                result = min(result, right-left)
        if result == len(nums) + 1:
            return 0
        else:
            return result