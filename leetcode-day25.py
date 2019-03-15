# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 21:11:56 2019

@author: Liurui
"""
"""
题目描述：  存在重复元素 II
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。

示例 1:

输入: nums = [1,2,3,1], k = 3
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1
输出: true
示例 3:

输入: nums = [1,2,3,1,2,3], k = 2
输出: false

思路：解法一为自己思路：解法二是查找表思路：结合使用滑动窗口和查找表，不断查找当前滑动窗口内有没有重复值。
我们通过建立一个 record 查找表，表中存的是窗口中的数，另外我们要注意的是，当窗口的大小 > k 的时候，
我们要移除 record 中最左边的元素（保证我们窗口中有 <= k 个数）。解法三为使用字典思路》
"""
class Solution1:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(set(nums)) == len(nums) or len(nums) <= 1:
            return False
        if len(nums) == 2:
            return 1 <= k
        for i in range(len(nums)-k):
            if nums[i] not in nums[i+1:i+k+1]:
                continue
            else:
                return True
        return len(set(nums[len(nums)-k:len(nums)])) < k
    

class Solution2:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        if (n <= 1):
            return False
        recode = set()
        for i in range(n):
            if nums[i] in recode:
                return True
            recode.add(nums[i])
            if len(recode) > k:
                recode.remove(nums[i - k])
        return False
class Solution:
    def containsNearbyDuplicate(self, nums: 'List[int]', k: 'int') -> 'bool':
        dic = {}
        
        for i in range(len(nums)):
            current = nums[i]
            if current in dic and i-dic[current] <= k:#{val : index}
                return True
            else:
                dic[current] = i
        
        return False   
    