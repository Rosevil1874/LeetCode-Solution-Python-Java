# 96 - 不同的二叉搜索树

## 题目描述
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?


## 动态规划
天哪[这个解答](https://leetcode.com/problems/unique-binary-search-trees/discuss/31666/)简直amazing，仔细看解释，虽然很大一段但是很清楚的。

```java
class Solution {
    public int numTrees(int n) {
        int[] G = new int[n + 1];
        G[0] = 1;
        G[1] = 1;

        for (int i = 2; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                G[i] += G[j - 1] * G[i - j];
            }
        }
        return G[n];
    }
} 
```
