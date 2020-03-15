# 493 - [逆序对](https://leetcode.com/problems/reverse-pairs/)

## 归并排序
遍历数组，把每一种和的出现次数保存起来，返回target出现的次数。

```python
from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        memo = {0:1}
        for x in nums:
            m = defaultdict(int)
            for curr_sum, cnt in memo.items():
                m[curr_sum + x] += cnt
                m[curr_sum - x] += cnt
            memo = m
        return memo[S]
```