# 22 - 括号生成


## 回溯法

>定义：
回溯法是一个**类似枚举的搜索尝试过程**，主要是在搜索过程中寻找问题的解，当发现不满足求解条件时，就**回溯**返回，尝试别的路径。

>回溯与递归：
回溯指的是一种**此路不通，绕道迂回**的算法思想，递归是代码层次上的一种组织结构。

回到此题中来，这个选择过程就是一种树结构。最开始的时候肯定只能选 (，因此，分析是从 ( 开始的。


```java
class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList();
        backtrack("", res, 0, 0, n);
        return res;
    }

    public void backtrack(String curr, List<String> res, int left, int right, int n) {
        if (right == n){
            res.add(curr);
            return;
        } 
        if (left < n) {
            backtrack(curr + '(', res, left + 1, right, n);
        } 
        if (right < left) {
            backtrack(curr + ')', res, left, right + 1, n);
        }
    }
}
```