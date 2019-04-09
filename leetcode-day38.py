# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 20:17:28 2019

@author: Liurui
"""
"""
题目描述：最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。

思路：解法一：最长的前缀不会超过最短的字符串，那么可以遍历最短的字符串的长度，依次比较。 
第一步：找出长度最短的字符串； 
第二步：依次与长度最短的字符串比较。
解法二：与解法一相同思路，不过有两个小改进：1： 找最短字符串长度采用min函数更加简洁
2：没有使用一个新的字符串，采用指针记录公共前缀位置，节省了空间 
解法三：运用os.path.commonprefix()函数
"""

class Solution1:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        if not strs:
            return ""
        lenth = len(strs[0])
        for i in range(len(strs)):
            if lenth > len(strs[i]):
                lenth = len(strs[i])
        for i in range(lenth):
            temp = strs[0][i]
            for s in strs[1:]:
                if s[i] != temp:
                    return res
            res += temp
        return res
    
class Solution2:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        minl = min([len(x) for x in strs])
        end = 0
        while end < minl:
            for i in range(1,len(strs)):
                if strs[i][end]!= strs[i-1][end]:
                    return strs[0][:end]
            end += 1
        return strs[0][:end]
    
class Solution3:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        import os
        return os.path.commonprefix(strs)
