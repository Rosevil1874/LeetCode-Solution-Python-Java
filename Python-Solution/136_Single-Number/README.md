# 136 - 只出现一次的数字

## 题目描述
![problem](images/136.png)

>关联题目： 
[137. 只出现一次的数字 II](https://github.com/Rosevil1874/LeetCode/tree/master/Python-Solution/136_Single-Number-II)
[260. 只出现一次的数字 III](https://github.com/Rosevil1874/LeetCode/tree/master/Python-Solution/260_Single-Number-III)


>审题：
出题人贴心给了两个小建议（还是小要求？）：  
1. 线性时间复杂度；
2. 不使用额外空间。  
线性时间复杂度倒容易满足，不使用额外空间就得想想了，毕竟要是可以用的话直接上collections.Counter就可以了哇。

## 题解一
没有思路，偷偷瞄了一眼相关话题，提到位运算和hash表，hash表不就是额外空间嘛，过。  
剩下位运算啦，**对于任何数x，都有x^x=0，x^0=x**，就是你了！so，一直往后异或，得到的结果就是我们要找的那个可怜巴巴的孤独的数了。

> Runtime: 84 ms, faster than 84.55% of Python3 online submissions.

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = 0
        for x in nums:
            single ^= x
        return single

```

后面都是借鉴的[Python different solutions](https://leetcode.com/problems/single-number/discuss/43000/Python-different-solutions.),这位老哥点子好多啊。首先是异或方法的one-line版：  

1. reduce + lambda

> Runtime: 76 ms, faster than 99.23% of Python3 online submissions

```python
from functools import reduce
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x^y, nums)
```

2. reduce + operator.xor

> Runtime: 88 ms, faster than 64.49% of Python3 online submissions.

```python
from functools import reduce
import operator
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(operator.xor, nums)
```

## 题解二
利用set的元素唯一的性质。

> Runtime: 76 ms, faster than 99.23% of Python3 online submissions.

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)
```
