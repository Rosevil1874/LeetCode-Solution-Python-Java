# 541 - 反转字符串 II

## 题目描述
![problem](images/541.png)

>关联题目： 
[344. 反转字符串](https://github.com/Rosevil1874/LeetCode/tree/master/Python-Solution/344_Reverse-String)
[557. 反转字符串中的单词 III](https://github.com/Rosevil1874/LeetCode/tree/master/Python-Solution/557_Reverse-Words-in-a-String-III)


## 题解一：
**思路：** 
1. 先实现一个转换整个字符串的函数；
2. 每次将字符串每2k个字符串中的前k个反转；
3. 将剩下的不足k个的字符串反转。

```python
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        n = len(s)        
        head = 0
        tail = head + k
        while tail <= n:
            self.reverseSubStr(s, head, head + k - 1)
            head += 2 * k
            tail = head + k
        
        self.reverseSubStr(s, head, n - 1)
            
        return ''.join(s)


    def reverseSubStr(self, s, i, j):
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
```

## 题解二：
emmmm可能因为刚刚从[344. 反转字符串](https://github.com/Rosevil1874/LeetCode/tree/master/Python-Solution/344_Reverse-String)过来的原因吧，看到这题的瞬间就想把上一题的解用上，完全忘记了还有现成的反转函数。。。人家循环也很漂亮，我的用变量head、tail去更新的方法也太笨拙太原始了吧so sad。。。

```python
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        for i in range(0, len(s), 2*k):
            s[i:i+k] = reversed(s[i:i+k])
        return ''.join(s)
```
