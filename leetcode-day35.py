# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 10:29:12 2019

@author: Liurui
"""
"""
题目描述： 字符串中的第一个唯一字符
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:

s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.
 

注意事项：您可以假定该字符串只包含小写字母。

思路：利用字典存储字符以及出现的次数，之后返回第一个出现次数为1的字符的下标
注意enumerate()以及get()函数的使用，可以简化程序
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = dict()
        for i in s:
            count[i] = count.get(i, 0) + 1
        for i, j in enumerate(s):
            if count.get(j) == 1:
                return i
        return -1