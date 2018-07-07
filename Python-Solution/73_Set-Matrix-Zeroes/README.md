# 73 - 矩阵置零

## 题目描述
![problem](images/73.png)


## 解法一
**空间复杂度max{O(m), O(n)}**

思路：
1. 遍历矩阵，遇到0元素则分别将其横纵坐标加入集合row、col；
2. 遍历集合row，将其代表的每一行置零；
3. 遍历集合col，将其代表的每一列置零。

```python
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
        	return None

        m = len(matrix)
        n = len(matrix[0])
        row = set()
        col = set()
        for i in range(m):
        	for j in range(n):
        		if matrix[i][j] == 0:
        			row.add(i)
        			col.add(j)

        for r in row:
        	matrix[r] = [0] * n
        for c in col:
        	for i in range(m):
        		matrix[i][c] = 0
```

## 解法二
**空间复杂度O(1)**

思路：
1. 把状态保存在第一行和第一列，即零元素所在行的第一个元素和所在列的第一个元素置零；
2. 使用单独的变量row0和col0保存第一行和第一列的状态；
3. 检查状态，根据状态改变矩阵。

```python
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
        	return None

        m = len(matrix)
        n = len(matrix[0])
        row0 = col0 = 1			# 第一列的状态
        for i in range(m):
        	for j in range(n):
        		if matrix[i][j] == 0:
        			if i == 0:
        				row0 = 0
        			if j == 0:
        				col0 = 0
        			matrix[i][0] = matrix[0][j] = 0

        for i in range(1, m):
        	for j in range(1, n):
        		if matrix[i][0] == 0 or matrix[0][j] == 0:
        			matrix[i][j] = 0

        if not row0:
        	matrix[0] = [0] * n

        if not col0:
        	for i in range(m):
        		matrix[i][0] = 0
```