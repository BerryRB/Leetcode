# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:10:57 2019

@author: 刘瑞
"""
"""
题目描述： 同构字符串
给定一个字符串，请将字符串里的字符按照出现的频率降序排列。

示例 1:

输入:
"tree"

输出:
"eert"

解释:
'e'出现两次，'r'和't'都只出现一次。
因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。
示例 2:

输入:
"cccaaa"

输出:
"cccaaa"

解释:
'c'和'a'都出现三次。此外，"aaaccc"也是有效的答案。
注意"cacaca"是不正确的，因为相同的字母必须放在一起。
示例 3:

输入:
"Aabb"

输出:
"bbAa"

解释:
此外，"bbaA"也是一个有效的答案，但"Aabb"是不正确的。
注意'A'和'a'被认为是两种不同的字符。

思路：同理用字典统计字符种类以及出现的次数，之后使用sorted函数对字典按值进行排序，之后将排序后的列表打印出来
"""
class Solution:
    def frequencySort(self, s: str) -> str:
        dict_s = {}
        res = ""
        char_s = []
        for i in s:
            dict_s[i] = dict_s.get(i, 0) + 1
        char_s = sorted(dict_s.items(),key = lambda x:x[1],reverse = True)
        for char in char_s:
            res += char[0]*char[1]
        return res 
