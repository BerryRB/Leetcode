# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 15:21:06 2019

@author: Liurui
"""
"""
题目描述：存在重复元素 III
给定一个整数数组，判断数组中是否有两个不同的索引 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值最大为 t，并且 i 和 j 之间的差的绝对值最大为 ķ。

示例 1:

输入: nums = [1,2,3,1], k = 3, t = 0
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1, t = 2
输出: true
示例 3:

输入: nums = [1,5,9,1,5,9], k = 2, t = 3
输出: false

思路：也是查找表与滑动窗口的思路：维持滑动窗的大小最大为 k，遍历每一个元素 nums[i]，在活动窗口中寻找 |one-nums[i]| < t，
即窗口中的元素范围为：[one-t … one+t] 之间。
"""
class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        lenth = len(nums)
        if lenth <= 1:
            return False
        a = set()
        for i in range(lenth):
            if t==0:
                if nums[i] in a:
                    return True
            else:
                for atem in a:
                    if abs(nums[i]-atem)<=t:
                        return True
            a.add(nums[i])
            if len(a) > k:
                a.remove(nums[i-k])
        return False