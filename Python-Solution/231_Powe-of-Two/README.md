# 231 - 2的幂

## 题目描述
![problem](images/231.png)

>关联题目： [326. 3的幂](https://github.com/Rosevil1874/LeetCode/tree/master/Python-Solution/326_Powe-of-Three)
>关联题目： [342. 4的幂](https://github.com/Rosevil1874/LeetCode/tree/master/Python-Solution/342_Powe-of-Four)


## 题解一：【除法运算】
**思路：** 最原始的方法，一直除以2，要是中间某个商是奇数肯定就不是2的幂啦可以直接返回False，或者一直顺利除下来除到商为1的时候就可以返回True啦。

```python
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:			# 1是2的幂
        	return True

        while n >= 1:
        	if n%2 == 1:
        		return False
        	elif n // 2 == 1:
        		return True

        	n = n // 2
```

优化一下：
```python
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
        	return False
        	
        while n%2 == 0:
        	n = n // 2
        return n == 1
```

来个one-line：
```python
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        return n > 0 and (n == 1 or (n % 2 == 0 and self.isPowerOfTwo(n // 2)))
```

## 题解二：【位运算】
**思路：** 2的幂的二进制表达里面只有最高位是1，而（2的幂-1）是全为1，比2的幂少一位。比如1000与0111。因此只要将n和n-1相与，若结果为0则n为2的幂。

```python
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and (n & (n - 1) == 0)
```