# 20 - 有效的括号

## 题目描述
![problem](images/20.png)

## 方法
数据结构经典题，用栈完美解决。
```python
class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        
        x = ['[', '(', '{']
        y = [']', ')', '}']
        z = ['[]', '()', '{}']
        
        stack = []
        for char in s:
            # 左括号入栈
            if char in x:
                stack.append(char)
            # 右括号判断栈中是否有与其匹配的左括号，有则将匹配的出栈，没有则返回false
            elif char in y:
                if stack == [] or stack.pop() + char not in z:
                    return False
            
        # 栈中左括号全部匹配，返回True
        return stack == []
```

使用栈和字典：
```python
class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        
        dic = {']': '[', ')': '(', '}': '{'}
        stack = []
        for char in s:
            # 左括号入栈
            if char in dic.values():
                stack.append(char)
            # 右括号判断栈中是否有与其匹配的左括号，有则将匹配的出栈，没有则返回false
            elif char in dic.keys():
                if stack == [] or dic[char] != stack.pop():
                    return False
            
        # 栈中左括号全部匹配，返回True
        return stack == []
```