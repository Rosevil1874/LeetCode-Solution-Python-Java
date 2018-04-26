# 54 - 螺旋矩阵

## 题目描述
![problem](images/54.png)

## 解法一
>按照螺旋形状寻找规律遍历。

思路：
1. 分别找到行列起止点rowBegin, rowEnd, colBegin, colEnd；
2. 向右遍历后rowBegin++，向下遍历后colEnd--，向左遍历后rowEnd--，向上遍历后colBegin++；
3. 直到行、列的起止点相遇；
4. 注意向左和向上遍历时需要检查此元素是否已经遍历过。

```python
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        n = len(matrix)
        
        if n == 0:
            return []
        
        rowBegin = 0
        rowEnd = n - 1
        colBegin = 0
        colEnd = len(matrix[0]) - 1
        
        while rowBegin <= rowEnd and colBegin <= colEnd:
			# 向右
            for j in range(colBegin, colEnd + 1):
				res.append(matrix[rowBegin][j])
            rowBegin += 1

			# 向下
            for i in range(rowBegin, rowEnd + 1):
				res.append(matrix[i][colEnd])
            colEnd -= 1

			# 向左
            j = colEnd
            while j >= colBegin and rowBegin <= rowEnd:
				res.append(matrix[rowEnd][j])
				j -= 1
            rowEnd -= 1

			# 向上
            i = rowEnd
            while i >= rowBegin and colBegin <= colEnd:
				res.append(matrix[i][colBegin])
				i -= 1
            colBegin += 1
            
        return res

```

## 解法二
矩阵操作
1. 转置： `list ( map(list, zip(*matrix)) )`
2. 反转： matrix.reverse()

>由于刚接触python，对这些基本结构的操作都不怎么了解，所以此方法是参考： [DP-solution-and-some-thoughts](https://leetcode.com/problems/maximum-subarray/discuss/20193/DP-solution-and-some-thoughts)。不足之处在于题意是按螺旋遍历，矩阵不变，而此解虽然非常取巧却把整个矩阵都删了。

思路：
1. 将矩阵第一行加入结果数组并删除；
2. 将矩阵转置并反转，就将最后一列翻转到了第一行；
3. 循环进行前两步。

```python
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        n = len(matrix)
        if n == 1:
            return matrix[0]
        while len(matrix) > 0:
            res += matrix[0]
            matrix.remove(matrix[0])
            matrix = list ( map(list, zip(*matrix)) )
            matrix.reverse()
        return res
```
