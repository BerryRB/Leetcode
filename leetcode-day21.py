# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 15:46:10 2019

@author: 刘瑞
"""
"""
题目描述：四数相加2
给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。

为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。

例如:

输入:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

输出:
2

解释:
两个元组如下:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

思路：将 A + B 的每一种可能放入查找表，然后 两重循环对在查找表中寻找是否存在 -(C[i] + D[i])，时间复杂度为 O(n^2)。两数相加的和作为键值。
"""
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        lenth, total_AB = len(A), {}
        for i in range(lenth):
            for j in range(lenth):
                total = A[i] + B[j]
                total_AB[total] = total_AB.get(total, 0) + 1
        res = 0
        for k in range(lenth):
            for l in range(lenth):
                total = C[k] + D[l]
                if -total in total_AB:
                    res += total_AB[-total]
        return res