# 22 - 括号生成

## 题目描述
![problem](images/22.png)

>审题：
看到括号生成不自觉会想到括号匹配的检查，在生成过程中也要注意匹配规范。

## 回溯法
cr:[leetcode-22-生成括号](https://blog.csdn.net/zjc_game_coder/article/details/78520742)

>定义：
回溯法是一个**类似枚举的搜索尝试过程**，主要是在搜索过程中寻找问题的解，当发现不满足求解条件时，就**回溯**返回，尝试别的路径。

>回溯与递归：
回溯指的是一种**此路不通，绕道迂回**的算法思想，递归是代码层次上的一种组织结构。

回到此题中来，下图可以说是非常直观了。这个选择过程就是一种树结构。最开始的时候肯定只能选 (，因此，分析是从 ( 开始的。
![backtracking](images/backtracking.png)

**私以为以下代码可以说是超级棒了**
```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.helper('', res, 0, 0, n)
        return res
    
    def helper(self, curr, res, left, right, n):
        # 当right == n 时说明已经有一个结果
        if right == n:
            res.append(curr)
        if left < n:
            self.helper(curr + '(', res, left + 1, right, n)
        if left > right:
            self.helper(curr + ')', res, left, right + 1, n)
```