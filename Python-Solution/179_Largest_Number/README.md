# 179 - 最大的数

## 题目描述
Given a list of non negative integers, arrange them such that they form the largest number.

**Example 1:**

	Input: [10,2]
	Output: "210"

**Example 2:**

	Input: [3,30,34,5,9]
	Output: "9534330"

**Note:** The result may be very large, so you need to return a string instead of an integer.


## 题解
```python
from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        key = cmp_to_key(lambda x, y: int(y + x) - int(x + y))
        nums = sorted(map(str, nums), key = key)
        return ''.join(nums).lstrip('0') or '0'
```
