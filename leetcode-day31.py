# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 22:10:31 2019

@author: Liurui
"""
"""
题目描述：有效的数独
判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。


上图是一个部分填充的有效的数独。

数独部分空格内已填入了数字，空白格用 '.' 表示。

示例 1:

输入:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
输出: true
示例 2:

输入:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
输出: false
解释: 除了第一行的第一个数字从 5 改为 8 以外，空格内其他数字均与 示例1 相同。
     但由于位于左上角的 3x3 宫内有两个 8 存在, 因此这个数独是无效的。
说明:

一个有效的数独（部分已被填充）不一定是可解的。
只需要根据以上规则，验证已经填入的数字是否有效即可。
给定数独序列只包含数字 1-9 和字符 '.' 。
给定数独永远是 9x9 形式的。

思路：主要方法可以总结为：1.检查每一行是否符合规范
2.检查每一列 
3.检查每一个3*3矩阵
难点在于如何对3*3进行准确分类，借鉴网上思路：只遍历一遍整个棋盘，可以通过i,j及地板除法来推断这个点在哪个3*3网格内。

解法二为解法一的简化版本，因为没有必要用dict,我们只某个数字关心有没有出现过。
"""
class Solution1:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
         dic_row = [{},{},{},{},{},{},{},{},{}]            # 每行的元素以一个字典储存，key是数字，value统一为1.
         dic_col = [{},{},{},{},{},{},{},{},{}]
         dic_box = [{},{},{},{},{},{},{},{},{}]

         for i in range(len(board)):
             for j in range(len(board)):
                 num = board[i][j]
                 if num == ".":
                     continue
                 if num not in dic_row[i] and num not in dic_col[j] and num not in dic_box[3*(i//3)+(j//3)]:
                     dic_row[i][num] = 1
                     dic_col[j][num] = 1
                     dic_box[3*(i//3)+(j//3)][num] = 1       # 利用地板除，向下取余。巧妙地将矩阵划分为九块
                 else:
                     return False

         return True
     
class Solution2:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        Cell = [[] for i in range(9)]                   # 没有必要用dict,我们只某个数字关心有没有出现过
        Col =  [[] for i in range(9)]
        Row =  [[] for i in range(9)]
        
        for i,row in enumerate(board):                  # 将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中
            for j,num in enumerate(row):
                if num != '.':
                    k = (i//3)*3 + j//3
                    if num in Row[i] + Col[j] + Cell[k]:    # list的骚操作,将三个list顺序的拼接 
                        return False
                    Row[i].append(num)
                    Col[j].append(num)
                    Cell[k].append(num)
                        
        return True


