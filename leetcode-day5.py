# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 22:20:09 2019

@author: 刘瑞
"""

"""
题目描述：
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:

给定 nums = [1,1,1,2,2,3],

函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,0,1,1,1,1,2,3,3],

函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3 。

你不需要考虑数组中超出新长度后面的元素。

思路：重点是如何判断连续三个及以上数字重复
解法1 用一个count计数，初始值设为1，重复一次加1，当count=3时说明有连续三个数字是重复的，
此时用pop弹出第三个重复的数字，count-1，当检测到相邻两个数不同时，count恢复初始值1，以此保持最多有两个重复数字；

解法2 是通过检测第i个数的前后数来判断是否有三个及以上数字重复，当第i个数等于第i+1个数但第i+1个数!=第i-1个数时说明有两个数字重复，
第i个数!=第i+1个数时说明没有数字重复，除此之外就是有连续3个及以上数字重复；

解法3 思路较为巧妙，通过判断第i个数是否大于第i-2个数来判断是否有连续三个及以上数字重复，大体思路和解法2类似，但写法与判断条件更为简洁。

"""
class Solution1:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=1
        i=0
        for _ in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                count+=1
                if count==3:
                    nums.pop(i)
                    count-=1
                else:
                    i+=1
            else:
                count=1
                i+=1
        return len(nums)
        
   

    
class Solution2:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if (n <= 2):
            return n
        # nums[0...i]是符合要求的，
        i = 1
        k = i - 1
        j = i + 1

        while j <= n-1:
            if (nums[j] != nums[i]) or (nums[j] == nums[i] and nums[j] != nums[k]):
                k = i
                nums[i+1] = nums[j]
                i += 1
            j += 1

        return i + 1

class Solution3:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for n in nums:
            if i < 2 or n > nums[i-2]:
                nums[i] = n
                i += 1
        return i   
