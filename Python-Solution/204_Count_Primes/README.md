# 204 - [计算质数](https://leetcode.com/problems/count-primes/)

## 题目描述
Count the number of prime numbers less than a non-negative number, n.


## 题解
[算法gif](https://assets.leetcode.com/static_assets/public/images/solutions/Sieve_of_Eratosthenes_animation.gif)

```python
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        prime = [True] * n
        prime[0] = prime[1] = False
        for i in range(2, int(n**0.5) + 1):
            if prime[i]:
                for j in range(i*i, n, i):
                    prime[j] = False
        return sum(prime)
        
```