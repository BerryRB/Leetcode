# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 17:01:31 2019

@author: 刘瑞
"""

"""
题目描述：回旋镖的数量
给定平面上 n 对不同的点，“回旋镖” 是由点表示的元组 (i, j, k) ，其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序）。

找到所有回旋镖的数量。你可以假设 n 最大为 500，所有点的坐标在闭区间 [-10000, 10000] 中。

示例:

输入:
[[0,0],[1,0],[2,0]]

输出:
2

解释:
两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]

思路：首先固定一个点，然后遍历这个点到其他点的距离，将距离作为键，此距离的个数作为值存到字典中，
则此固定点的回旋镖个数为（距离的个数）*（距离的个数-1）
***理解为固定完一个点后，剩余了两个位置，其余所有的点在这两个位置上进行排列组合，由于固定的点到本身距离为0，而距离为0的点只有一个，
无法放到两个位置中去，所以此情况得到的回旋镖个数为0，则此种情况在程序中不需要进行i!=j的判断***
"""
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        for i in points:
            hashmap = dict()
            for j in points:
                x, y = i[0]-j[0], i[1]-j[1]
                dist = x*x + y*y
                hashmap[dist] = hashmap.get(dist, 0) + 1
            for value in hashmap:
                res += hashmap[value]*(hashmap[value]-1)
        return res
