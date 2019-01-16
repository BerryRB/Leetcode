# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 22:14:44 2019

@author: 刘瑞
"""

"""
题目描述：验证回文字符串
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false

思路：同样是对撞指针思路，注意使用python字符处理的内置函数
"""
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = [i for i in s.lower() if i.isalnum()] 
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l]  == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True