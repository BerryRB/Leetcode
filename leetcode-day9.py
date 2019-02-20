# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 21:35:31 2019

@author: 刘瑞
"""

"""
题目描述：反转字符串中的元音字母
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

示例 1:

输入: "hello"
输出: "holle"
示例 2:

输入: "leetcode"
输出: "leotcede"
说明:
元音字母不包含字母"y"。

思路：对撞指针思路，注意list函数与join函数的使用
"""
class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        value = ['a','e','i','o','u']
        l, r = 0, len(s) - 1
        s = list(s)
        while l < r:
            if s[l].lower() in value and s[r].lower() in value:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            if s[l].lower() not in value:
                l += 1
            if s[r].lower() not in value:
                r -= 1
        return ''.join(s)