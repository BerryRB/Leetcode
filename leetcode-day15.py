# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 09:36:49 2019

@author: 刘瑞
"""
"""
题目描述：两个数组的交集2
给定两个数组，编写一个函数来计算它们的交集。

示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]
示例 2:

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]

说明：
输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
我们可以不考虑输出结果的顺序。

思路：利用字典的键储存nums1数字的值，利用字典的值统计数字出现的次数，然后遍历nums2，若nums2的数字在字典中出现则将相应的键加入结果列表中，
并将数字出现的次数减1，出现次数为0时不再统计该数字
"""
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = {}
        res = []
        for num in nums1:
            counts[num] = counts.get(num, 0) + 1
        for num in nums2:
            if num in counts and counts[num] > 0:
                res.append(num)
                counts[num] -= 1
        
        return res