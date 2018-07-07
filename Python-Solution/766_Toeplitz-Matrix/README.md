# 766 - 托普利茨矩阵

## 题目描述
![problem](images/766.png)

>审题：  
题目表达不清晰，应该是由左上到右下的对角线上**元素相同**，而不是只要有相同元素就行了。

## 题解一
思路：
emmm就是根据规则一个个判断就行了。

```python
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for i in range(len(matrix) - 1):
            for j in range(len(matrix[0]) - 1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
        return True
```

## 题解二
> cr: [One Line Easy Python Solution, Using Slice. Only 1 "For Loop"](https://leetcode.com/problems/toeplitz-matrix/discuss/113411/One-Line-Easy-Python-Solution-Using-Slice.-Only-1-%22For-Loop%22.)

思路：  
找规律小能手哈哈，假设每一行的元素个数为n，符合规则的矩阵每一行的前n-1个元素与下一行的后n-1个元素相同，就酱！

```python
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for i in range(len(matrix) - 1):
            if matrix[i][:-1] != matrix[i+1][1:]:  
                return False
        return True
```

一行代码：  
```python
return all(matrix[i][:-1] == matrix[i+1][1:] for i in range(len(matrix) - 1))
```