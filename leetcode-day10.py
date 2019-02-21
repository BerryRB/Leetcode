# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 10:21:51 2019

@author: 刘瑞
"""
"""
题目描述：盛最多水的容器
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

示例:

输入: [1,8,6,2,5,4,8,3,7]
输出: 49

思路：采用对撞指针，计算可能存在的最大面积，首先计算第一列和最后一列所围的面积，此时剩余的容器若想面积比此容器大，
则必须有一条高大于两条高中相对较小的那条高。按照此思路每次更新两条高中较小的那条，依次计算面积并最更新最大面积，直至两条高相遇。

"""
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height)-1
        volume = 0
        while left < right:
            volume = max(volume, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return volume