# 301 - [删除无效的括号](https://leetcode.com/problems/remove-invalid-parentheses/)

## 题目描述
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).


## 1. DFS 

```python
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = []
        self.remove(s, 0, 0, '(', ')', res)
        return res
    
    
    def remove(self, s: str, start_to_count: int, start_to_remove: int, open_p: str, close_p:str, res: List[str]):
        cnt = 0             # 模拟出栈入栈检查括号是否匹配
        # 从前到后删除多余的')'
        for i in range(start_to_count, len(s)):
            if s[i] == open_p:
                cnt += 1
            elif s[i] == close_p:
                cnt -= 1
            if cnt >= 0:  # 括号匹配：'('比')'多
                continue
                
            # 在start_to_count到i(包括i)之间')'比'('多，删除多余的')'
            for j in range(start_to_remove, i + 1):
                if s[j] == close_p and (start_to_remove == j or s[j - 1] != close_p):
                    self.remove(s[:j] + s[j+1:], i, j, open_p, close_p, res)
            return
            
        # 反转字符串删除多余的'('
        reversed_s = s[::-1]
        if open_p == '(':
            self.remove(reversed_s, 0, 0, ')', '(', res)
        else:
            res.append(reversed_s)
```

## 2. BFS
