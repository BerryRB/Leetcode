# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 20:05:51 2019

@author: 刘瑞
"""
"""
题目描述：
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:

返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
示例:

输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。

思路：对撞指针法
们首先判断首尾两项的和是不是 target，如果比 target 小，那么我们左边 (i)+1 位置的数（比左边位置的数大）再和右相相加
，继续判断。如果比 target 大，那么我们右边 (j)-1 位置的数（比右边位置的数小）再和左相相加，继续判断。
我们通过这样不断放缩的过程，就可以在 O(n) 的时间复杂度内找到对应的坐标位置。
"""
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(nums)-1
        while left < right :
            sum_num = nums[left] + nums[right]
            if sum_num == target:
                return [left+1, right+1]
            elif sum_num < target:
                left += 1
            else:
                right -= 1
        return []