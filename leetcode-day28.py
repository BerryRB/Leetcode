# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 21:57:52 2019

@author: Liurui
"""
"""
题目描述：买卖股票的最佳时机 II
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释: 
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]
说明:

尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
要求使用空间复杂度为 O(1) 的原地算法。

思路：解法一为翻转数组法：
解析：如下过程，先翻转前n-k个字符，在翻转后k个字符，最后将整个字符串翻转，一共三次逆置
1 2 3 4 5 6 7
4 3 2 1 5 6 7
4 3 2 1 7 6 5
5 6 7 1 2 3 4
解法二为利用python内置函数大偷懒解法，时间效率不高
"""

class Solution1:
    def rotate(self, nums, k):
        def numReverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        k, n = k % len(nums), len(nums)
        if k:
            numReverse(0, n - 1)
            numReverse(0, k - 1)
            numReverse(k, n - 1)

class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            nums.insert(0,nums.pop())