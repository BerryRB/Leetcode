# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:45:57 2019

@author: 刘瑞
"""
"""
题目描述：字母异位词分词
给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。

示例 1:

输入: [[1,1],[2,2],[3,3]]
输出: 3
解释:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4
示例 2:

输入: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
输出: 4
解释:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6

思路：两点可以确定一条直线，那么选择固定一个点，求其他点与固定点的斜率，如果斜率相同，那么斜率相同的点在同一条直线上。
同时要考虑，斜率可能为无穷大，也有可能两个点为同一个点。键值应该为：斜率。
***注意求斜率为两个数相除，需注意精度问题，1、可改为分母格式（用gcd函数求最大公约数/2、用Decimal函数 3、用numpy 的float64数据类型***
"""
# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) < 3:
            return len(points)
        res = 0
        for i in range(len(points)-1):
            h, same_point = {'inf':0}, 1
            x1, y1 = points[i].x, points[i].y
            for j in range(i + 1, len(points)):
                x2, y2 = points[j].x, points[j].y
                if x1 == x2 and y1 == y2:
                    same_point += 1
                elif x1 == x2:
                    h['inf'] += 1
                else:
                    slope = (y2 - y1) * 100.0 / (x2 - x1)
                    h[slope] = h.get(slope, 0) + 1
            res = max(res, (max(h.values()))+same_point)   
        return res
                
