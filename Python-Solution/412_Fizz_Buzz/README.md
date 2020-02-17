# 412 - Fizz Buzz


### 1. 模运算 %
```python
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return [('Fizz') * (not i % 3) + ('Buzz') * (not i % 5) or str(i) for i in range(1, n + 1)]
```

### 2. 不使用模运算
```python
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        fizz, buzz = 0, 0
        for i in range(1, n + 1):
            fizz += 1
            buzz += 1
            if fizz == 3 and buzz == 5:
                res.append('FizzBuzz')
                fizz, buzz = 0, 0
            elif fizz == 3:
                res.append('Fizz')
                fizz = 0
            elif buzz == 5:
                res.append('Buzz')
                buzz = 0
            else:
                res.append(str(i))
        return res
```
