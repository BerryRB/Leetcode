# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 11:20:35 2019

@author: 刘瑞
"""
"""
题目描述：(荷兰国旗问题)
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:

输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]

思路：
解法1 两趟扫描算法：首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
解法2 一趟扫描算法：思路如下：将前部和后部各排在数组的前边和后边，中部自然就排好了。具体的：
设置两个标志位begin和end分别指向这个数组的开始和末尾，然后用一个标志位current从头开始进行遍历：
1）若遍历到的位置为0，则说明它一定属于前部，于是就和begin位置进行交换，然后current向前进，begin也向前进（表示前边的已经都排好了）。
2）若遍历到的位置为1，则说明它一定属于中部，根据总思路，中部的我们都不动，然后current向前进。
3）若遍历到的位置为2，则说明它一定属于后部，于是就和end位置进行交换，由于交换完毕后current指向的可能是属于前部的，若此时current前进则会导致该位置不能被交换到前部，所以此时current不前进。而同1），end向后退1。
"""
class Solution1:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count1 = nums.count(0)
        count2 = nums.count(1)
        count3 = nums.count(2)
        nums[:count1] = [0]*count1
        nums[count1:count1+count2] = [1]*count2
        nums[count1+count2:] = [2]*count3
        
class Solution2:
    def sortColors(self, nums):
        begin, current, end = 0, 0, len(nums) - 1   
        
        while current <= end:
            if nums[current] < 1:
                nums[begin], nums[current] = nums[current], nums[begin]
                current += 1
                begin += 1
            elif nums[current] > 1:
                nums[current], nums[end] = nums[end], nums[current]
                end -= 1
            else:
                current += 1

                
                