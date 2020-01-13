# 338 - [比特位计数](https://leetcode.com/problems/counting-bits/)

## 题目描述
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

**Example 1:**
	Input: 2
	Output: [0,1,1]
**Example 2:**
	Input: 5
	Output: [0,1,1,2,1,2]
**Follow up:**
	- It is very easy to come up with a solution with run time O(n\*sizeof(integer)). But can you do it in linear time **O(n)** /possibly in a **single pass**?
	- Space complexity should be **O(n)**.
	- Can you do it like a boss? Do it without using any builtin function like `__builtin_popcount` in c++ or in any other language.


## 题解
分奇数和偶数讨论，分别举个例子就很好理解：
1. 奇数：
	111010**1**
	111010**0**
2. 偶数：
	101101**0**
	101101
	
```python
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0] * (num + 1)
        for i in range(1, num + 1):
            if i % 2 == 1:
                res[i] = res[i - 1] + 1
            else:
                res[i] = res[i >> 1]
        return res
```