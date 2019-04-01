# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 22:13:18 2019

@author: Liurui
"""
"""
题目描述：实现strStr()
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1
说明:

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。

思路：遍历haystack的每个字符，运用切片判断第i个字符及后面第i+len(needle)个字符是否符合条件，类似于滑动窗口
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lenth = len(needle)
        if lenth == 0:
            return 0
        if  lenth > len(haystack):
            return -1
        for i in range(len(haystack)):
            if haystack[i:i+lenth] == needle:
                return i
        return -1