# 7 - 颠倒整数

## 题目描述
![problem](images/7.png)

<!-- more -->

## 一、字符串反转
>看到题目，想到三个要注意的点：
1. 负数的处理；
2. 原数末尾为零时颠倒后要去掉；
3. 如何检查32位整数的溢出。

解决：
1. 给负数立个flag（没错就是立flag哈哈），然后绝对值化再处理，最后返回时给原本是负号的再负一下就行了；
2. 判断判断就行，末尾有零的给他去掉；
3. 笨方法就是直接判断有没有超过32位整数范围（-2147483648 ~ 2147483647），但是暂时还没想到不笨的方法（python的弱类型啊啊啊）

```python
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if -10 < x < 10:
            return x
            
        # 1.判断是否为负数
        flag = False  
        if x < 0:
            x = -x
            flag = True

        # 2. 转化为字符串翻转
        x = str(x)[::-1]

        # 3. 去掉多余的零
        while x[0] == '0':
            x = x[1:]

        # 4. 转化为整数并判断溢出
        x = int(x)
        if flag:
            x = -x
        if -2147483648 < x < 2147483647:
            return x
        else:
            return 0
```

**一开始忽略了只有一位的情况，这种情况直接返回就好~~**


## 二、 字符串反转--简化版（大神版）
```python
class Solution:
    def reverse(self, x: int) -> int:
        s = (x > 0) - (x < 0)       # 符号位
        r = int(str(s*x)[::-1])     # 绝对值反转
        return s*r * (r < 2**31)
```python


## 按位反转  
依次将最后一位插入到返回数字的最前面，每插入一次之前判断此次插入是否会导致溢出。
```python
class Solution:
    def reverse(self, x: int) -> int:
        sign = (x > 0) - (x < 0)
        x = x * sign
        res = 0
        while x > 0:
            res = res * 10 + x % 10
            x = x // 10
        return sign * res * (res < 2**31)
```python