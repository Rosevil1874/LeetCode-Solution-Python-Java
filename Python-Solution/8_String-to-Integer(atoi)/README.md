# 8 - 字符串转整数

## 题目描述
![problem](images/8.png)

<!-- more -->

## 方法
>嗯要注意的地方题目上已经说得非常明白了，一个一个care就好啦。

```python
class Solution:
    def myAtoi(self, str):
        # 去掉空白符
        str = str.strip()
        if not len(str):
            return 0

        # 确定符号位
        sign = 1
        start = 0   # 开始判断数字的索引
        if str[0] == '+':
            sign = 1
            start = 1
        elif str[0] == '-':
            sign = -1
            start = 1

        is_valid = False    # 从符号位开始，后面是否接数字
        res = 0
        for i in range(start, len(str)):
            if str[i] >= '0' and str[i] <= '9':
                is_valid = True
                res = res * 10 + int(str[i])
            else:
                break

        res = sign * res
        # 若符号位后不是紧跟数字则无效
        if not is_valid:
            return 0
        # 检查是否溢出
        elif res > 2**31 - 1:
            return 2**31 - 1
        elif res < -2**31:
            return -2**31
        else:
            return res
```