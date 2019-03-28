# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 11:26:21 2019

@author: Liurui
"""
"""
题目描述：整数反转
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

思路：利用列表切片[::-1]
"""
class Solution:
    def reverse(self, x: int) -> int:
        res = list(str(x))[::-1]
        if res[-1] == "-":
            res.insert(0, res.pop())
        res = int("".join(res))
        if res < -2147483648 or res > 2147483647:
            res = 0
        return res