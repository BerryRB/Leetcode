# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 21:47:47 2019

@author: 刘瑞
"""

"""
题目描述： 同构字符串
给定两个字符串 s 和 t，判断它们是否是同构的。

如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。

所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

示例 1:

输入: s = "egg", t = "add"
输出: true
示例 2:

输入: s = "foo", t = "bar"
输出: false
示例 3:

输入: s = "paper", t = "title"
输出: true
说明:
你可以假设 s 和 t 具有相同的长度。

思路：可以使用字典 dict 来记住这些字符对。用两个字典 dict，一个字典 lookup1 用来记 s 的字符到 t 的映射，
另一个字典 lookup2 用来记录 t 的字符到 s 的映射，用于判断 t 中的两个字符不能由 s 中同一个字符映射而来。
***另外注意掌握zip函数的用法,采用zip函数有一行代码解决方案
"""

class Solution:
    def isIsomorphic(self, s, t):
        lookup1, lookup2 = {}, {}
        for i in range(len(s)):
            if s[i] not in lookup1:
                lookup1[s[i]] = t[i]
            if t[i] not in lookup2:
                lookup2[t[i]] = s[i]
            if lookup1[s[i]] != t[i] or lookup2[t[i]] != s[i]:
                return False
        return True