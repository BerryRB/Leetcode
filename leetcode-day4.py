# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 16:07:03 2019

@author: 刘瑞
"""
"""
题目描述：
给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

示例 1:

给定 nums = [3,2,2,3], val = 3,

函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,1,2,2,3,0,4,2], val = 2,

函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。

注意这五个元素可为任意顺序。

你不需要考虑数组中超出新长度后面的元素。

思路：判断通过利用python的切片操作，理解切片是原地操作。
"""

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums[:]=[i for i in nums if i!=val]
        return len(nums)
    
    
nums=[1,1,2,3,4,4,3,2]
val=2
test=Solution()
result=test.removeElement(nums,val)
print(nums)
print(result)