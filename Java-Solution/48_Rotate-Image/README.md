# 48 - 旋转图像

## 题目描述
![problem](images/48.png)

>审题：
1. 矩阵顺时针旋转90°；
2. 原地操作，无返回参数。

## 环形旋转
这道题可以说是非常经典了，会不会每新学一门语言就要再写一次啊_(°ω°｣∠)_  不过以前是直接将矩阵旋转90°输出，而不是改变原矩阵。那么就用交换吧，emmm但是看了一下，交换的话得同时交换四个方向的元素，好麻烦啊啊啊。

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # 环形旋转
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                matrix[i][j], matrix[j][n-i-1], matrix[n-i-1][n-j-1], matrix[n-j-1][i] = matrix[n-j-1][i], matrix[i][j], matrix[j][n-i-1], matrix[n-i-1][n-j-1]

```


## 反转+对角线交换
>cr: [A common method to rotate the image](https://leetcode.com/problems/rotate-image/discuss/18872/A-common-method-to-rotate-the-image)

一、顺时针旋转90°
1. 上下翻转；
2. 对角线对换。

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 上下翻转
        matrix.reverse()
        
        # 对角线对换
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
```


二、逆时针旋转90°
1. 左右翻转；
2. 对角线对换。
```python
# 左右反转
for i in range(len(matrix)):
    width = len(matrix[i])
    for j in range( width // 2 ):
        matrix[i][j], matrix[i][width-j-1] = matrix[i][width-j-1], matrix[i][j]

# 对角线对换
for i in range(len(matrix)):
    for j in range(i+1, len(matrix[i])):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
```