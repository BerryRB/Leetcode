# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 10:35:49 2019

@author: Liurui
"""
"""
题目描述：有效的数独
给定一个 n × n 的二维矩阵表示一个图像。

将图像顺时针旋转 90 度。

说明：

你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

示例 1:

给定 matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
示例 2:

给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

思路：首先将矩阵转置，转置后将矩阵按列进行翻转既得旋转90度后的图像
1、***掌握[start:end:-1]进行翻转的方法，其中-1表示为步长***
2、****掌握方法二中利用zip函数进行矩阵转置的方法，其中zip()返回的为元祖，利用map函数将其转化为列表***
"""
class Solution1:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        num= len(matrix)
        for i in range (0,num):
            for j in range(i+1,num):
                matrix[i][j], matrix[j][i] =matrix[j][i], matrix[i][j]
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]

class Solution2:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = map(list, zip(*matrix[::-1]))

