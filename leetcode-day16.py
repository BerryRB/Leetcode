# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 14:48:48 2019

@author: 刘瑞
"""
"""
题目描述： 有效的字母异位词
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母

思路：利用字典统计出现的字母种类及次数，然后利用operator的比较函数对字典进行比较，相同则True。
同时注意掌握collections的Counter函数，可快速对字符进行统计。
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts1, counts2 = {}, {}
        strs1, strs2 = list(s), list(t)
        for i in strs1:
            counts1[i] = counts1.get(i, 0) +1
        for j in strs2:
            counts2[j] = counts2.get(j, 0) +1
        return (operator.eq(counts1, counts2))