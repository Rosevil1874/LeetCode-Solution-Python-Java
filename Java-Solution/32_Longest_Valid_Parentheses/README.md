# 32 - 最长有效括号

## 题目描述

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"



## 一、栈
思路：
1. 从前往后遍历字符串；
2. 若当前为字符'('则将其下标入栈，否则将栈顶出栈(此时找到了一对有效括号)；
3. 若出栈后栈空则将')'的下标入栈，否则计算当前匹配的括号长度并更新最长匹配长度；
```Java
class Solution {
    public int longestValidParentheses(String s) {
        int maxRes = 0;
        Stack<Integer> stack = new Stack<>();
        stack.push(-1);

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                stack.push(i);
            } else {
                stack.pop();
                if (stack.empty()) {
                    stack.push(i);
                } else {
                    maxRes = Math.max(maxRes, i - stack.peek());
                }
            }
        }
        return maxRes;
    }
}
```


## 二、动态规划

let dp[i] is the number of longest valid Parentheses ended with the i - 1 position of s, then we have the following relationship:
**dp[i + 1] = dp[p] + i - p + 1** where p is the position of '(' which can matches current ')' in the stack.

```java
class Solution {
    public int longestValidParentheses(String s) {
        int maxRes = 0;
        int dp[] = new int[s.length() + 1];
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                stack.push(i);
            } else {
                if (!stack.empty()) {
                    int p = stack.pop();
                    dp[i + 1] = dp[p] + i - p + 1;
                    maxRes = Math.max(maxRes, dp[i + 1]);
                }
            }
        }
        return maxRes;
    }
}
```
