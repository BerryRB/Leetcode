# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:39:46 2019

@author: 刘瑞
"""

"""
题目描述：四数之和
给定一个整数数组，判断是否存在重复元素。

如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。

示例 1:

输入: [1,2,3,1]
输出: true
示例 2:

输入: [1,2,3,4]
输出: false
示例 3:

输入: [1,1,1,3,3,4,3,2,4,2]
输出: true


"""
class Solution:
    def fourSum(self, nums, target):
        def findNsum(nums, target, N, cur):
            if len(nums) < N or N < 2 or nums[0] * N > target or nums[-1] * N < target:  # if minimum possible sum (every element is first element) > target 
                return  # or maximum possible sum (every element is first element) < target, it's impossible to get target anyway          
            if N == 2:  # 2-sum problem
                l, r = 0, len(nums) - 1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        res.append(cur + [nums[l], nums[r]])
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else:  # reduce to N-1 sum problem
                for i in range(len(nums) - N + 1):
                    if i == 0 or nums[i - 1] != nums[i]:
                        findNsum(nums[i + 1 :], target - nums[i], N - 1, cur + [nums[i]])

        res = []
        findNsum(sorted(nums), target, 4, [])
        return res