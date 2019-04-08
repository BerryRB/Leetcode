# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 20:42:41 2019

@author: Liurui

"""
"""
题目描述：报数
报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。

注意：整数顺序将表示为一个字符串。

 

示例 1:

输入: 1
输出: "1"
示例 2:

输入: 4
输出: "1211"

思路：递归思想，根据报数的特点，我们可以根据上一项的结果推导下一项。我们遍历上一项，辅以计数变量count统计一下某些数字出现的次数,
同时我们要不断保存上一项。
"""
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        if n == 2:
            return "11"
        pre = "11"
        for _ in range(2,n):
            res = ""
            count = 1
            last = pre[0]
            for s in pre[1:]:
                if s == last:
                    count += 1
                else:
                    res += str(count) + last
                    last = s
                    count = 1
            res += str(count) + last
            pre = res
        return res