# 91 - [解码方法](https://leetcode.com/problems/decode-ways/)


## DP
```python
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        # dp[i]: decode way fors[1:i + 1]
        dp = [0 for _ in range(len(s) + 1)]
        dp[0:2] = [1, 1]    # base case
        
        for i in range(2, len(s) + 1):
            # one step jump
            if 0 < int(s[i - 1:i]) <= 9:
                dp[i] += dp[i - 1]
            # two steps jump
            if 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[-1]
```
