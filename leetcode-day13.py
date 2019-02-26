# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 16:19:46 2019

@author: 刘瑞
"""

"""
题目描述：快乐数
编写一个算法来判断一个数是不是“快乐数”。

一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。

示例: 

输入: 19
输出: true
解释: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

思路：重点是如何判断无限循环，若某一次求平方和的结果重复出现就说明陷入了无限循环。
注意set的添加元素用add函数,列表的添加用append函数
"""

class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        ss = set()
        while True:
            if n == 1:
                return True
            total = 0
            while n:
                total += (n % 10) * (n %10)
                n = n // 10
            if total in ss:
                return False

            ss.add(total)
            n = total