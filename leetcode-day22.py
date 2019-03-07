# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 15:10:31 2019

@author: 刘瑞
"""
"""
题目描述：字母异位词分词
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：

所有输入均为小写字母。
不考虑答案输出的顺序。

思路：对字符串数组中每一个字符串进行排序，之后如果遇到相等的字符串，就说明该字符串对应的排序前的字符串是字母易位词。
找字母易位词的过程用哈希表，每当出现一个新的字母易位词，就往 ret 中添加一个 list，同时往哈希表中添加该字母易位词，
并将该字母易位词在哈希表中的 value 值存成该 list 的索引值；出现哈希表中已经存在的字母易位词，直接往对应索引的 list 中添加即可。
排序后的字符串作为键值。
"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dt = dict()
        for st in strs:
            t = ''.join(sorted(st))
            if t in dt:
                dt[t].append(st)
            else:
                dt[t] = [st]
        return list(dt.values())