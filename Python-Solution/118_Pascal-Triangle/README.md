# 118 - 杨辉三角

## 题目描述
![problem](images/118.png)

>关联题目： [119. 杨辉三角 II](https://github.com/Rosevil1874/LeetCode/tree/master/Python-Solution/119_Pascal's-Triangle-II)

## 解法一
思路：  
emmm就是老老实实按照杨辉三角的构造规则构造一个( ･´ω\`･)  


```python
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ret = []
        if numRows == 0:
        	return ret
        for i in range(1, numRows + 1):
        	nums = [1] * i
        	if i > 2:
        		for j in range(1, i - 1):
        			nums[j] = ret[i - 2][j - 1] + ret[i - 2][j]
        	ret.append(nums)
        return ret
```

## 解法二
>cr: [Python 4 lines short solution using map.](https://leetcode.com/problems/pascals-triangle/discuss/38128/Python-4-lines-short-solution-using-map.)
厉害了，我找了半天规律也只能从等差数列的思路下手，人家把数组一错开就OK了(눈‸눈)  
![idea](images/idea.png)

```python
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
        	return []
        ret = [[1]]
        for i in range(1, numRows):
        	ret.append( list( map(lambda x,y: x+y, ret[-1] + [0], [0] + ret[-1]) ) )
        return ret
```