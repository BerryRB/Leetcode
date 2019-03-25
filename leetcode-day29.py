# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:06:02 2019

@author: Liurui
"""
"""
题目描述：只出现一次的数字
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4

思路：我们可以考虑 异或运算 ，它是满足交换律和结合的，也就是说 a^b^c = a^c^b，同时0异或任何数结果不变，这样当我们遍历数组，
顺次进行异或运算，那么最终的结果就是唯一的不重复数字。
如[4,1,2,1,2]，4^1^2^1^2 = 1^1^2^2^4 = 0^0^4=4
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            result = result ^ nums[i]
        return result