# 166 - 分数到小数

## 题目描述
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

**Example 1:**
	Input: numerator = 1, denominator = 2
	Output: "0.5"

**Example 2:**
	Input: numerator = 2, denominator = 1
	Output: "2"

**Example 3:**
	Input: numerator = 2, denominator = 3
	Output: "0.(6)"

## 题解
老老实实按照除法顺序判断。：
1. 边界条件：被除数为0时结果为0，被除数与除数符号不一致时结果为负数；
2. 计算整数部分结果，若此时余数为零则可直接返回结果；
3. 计算小数部分，按照除法计算方法循环计算每一位余数，同时将每一位余数的位置存储在hash表中，若有重复出现的小数部分则说明为循环小数，将循环部分加上括号即可返回。否则一直除到余数为0. 

**迭代1**
```python
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        
        # 判断符号位
        sign = '-' if numerator * denominator < 0 else ''
        # 整数部分，余数
        numerator, denominator = abs(numerator), abs(denominator)
        n, remainder = divmod(numerator, denominator)
        if remainder == 0:
            return sign + str(n)
        res = sign + str(n) + '.'
        
        # 计算小数部分    
        hashtable = {}
        i = len(res)
        while remainder != 0:
            if remainder not in hashtable:
                hashtable[remainder] = i
            else:
                i = hashtable[remainder]
                res = res[:i] + '(' + res[i:] + ')'
                return res
            n, remainder = divmod(remainder * 10, denominator)
            res += str(n)
            i += 1
            
        return res

```