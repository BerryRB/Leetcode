# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 10:39:20 2019

@author: Liurui
"""

"""
题目描述：加一
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。

思路：解法一：将数组中的各位数字提取为一个整数，进行整数加一运算后再将数字各位分开存放到数组中，Solution1和Solution2
为此种思路的两种写法，注意学习Solution1中字符串的思想，此种写法较为简洁

解法二：我们需要判断会不会产生进位的情况,所以我们可以设置一个状态变量 carry
当它为1的时候,就说明当前位数值需要加1
当当前位数值为9时,加1就需要进一位,即 carry 仍为1,否则 carry 赋值为0
倒序遍历数组
最后判断 carry 为1或者0,为1时,在数组头部加1
"""
class Solution1:
    def plusOne(self, digits):
        s = ''
        for i in digits:  # 转化成字符串
            s += str(i)
        s = int(s) + 1    
        return [int(x) for x in str(s)]
    
class Solution2:
    def plusOne(self, digits: List[int]) -> List[int]:
        num, lenth = 0, len(digits)
        for i in range(lenth):
            num = num + digits[i]*(pow(10,(lenth-1-i)))
        num += 1
        for i in range(lenth):
            digits[i] = (num//pow(10,(lenth-1-i)))
            num = num % pow(10,(lenth-1-i))
        if digits[0] == 10:
            digits[0] = 0
            digits.insert(0,1)
        return digits
    
class Solution3:
    def plusOne(self, digits):
        carry=1
        l = len(digits)
        for x in range(-1,-l-1,-1):
            if(digits[x]==9 and carry==1):
                digits[x]=0
                carry = 1 
            elif(carry==1):
                digits[x] += 1
                carry = 0
        if(carry==1):
            digits.insert(0, 1)
        return digits