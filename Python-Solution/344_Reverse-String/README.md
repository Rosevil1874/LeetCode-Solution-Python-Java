# 344 - 反转字符串

## 题目描述
![problem](images/344.png)

>关联题目： 
[541. 反转字符串 II](https://github.com/Rosevil1874/LeetCode/tree/master/Python-Solution/541_Reverse-String-II)

>题目要求：
1. 原地修改输入数组，不返回任何内容；
2. 使用 O(1) 的额外空间.

## 题解一：【按序插入】
**思路：** 以原字符串的最后一个字母为基准，每次将字符串当前的第一个字母插入到基准字母后面，遍历完一遍字符串就好啦。

```python
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i = len(s) - 1
        while i > 0:
            x = s.pop(0)
            s.insert(i, x)
            i -= 1
```


## 题解二：【交换】
**思路：** 每次将字符串前面一半的元素与后面一半对应位置的元素交换位置。

```python
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
```