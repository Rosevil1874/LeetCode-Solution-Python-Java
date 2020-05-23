# 72 - 编辑距离

## 题目描述
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

- Insert a character
- Delete a character
- Replace a character



## 递归
测试用例长度达到：
- word1："dinitrophenylhydrazine"
- word2："acetylphenylhydrazine"

就超时了，`Time Limit Exceeded`。

```java
class Solution {
    public int minDistance(String word1, String word2) {
        int m = word1.length(), n = word2.length();
        if (m == 0 && n == 0) {
            return 0;
        } else if (m == 0) {
            return n;
        } else if (n == 0) {
            return m;
        } else if (word1.charAt(0) == word2.charAt(0)) {
            return minDistance(word1.substring(1), word2.substring(1));
        }

        int insert = 1 + minDistance(word1, word2.substring(1));
        int delete = 1 + minDistance(word1.substring(1), word2);
        int replace = 1 + minDistance(word1.substring(1), word2.substring(1));
        return Math.min(insert, Math.min(delete, replace));

    }
}
```

### 动态规划

```java
class Solution {
    public int minDistance(String word1, String word2) {
        int m = word1.length(), n = word2.length();
        // 至少其中一个为0
        if (m * n == 0){
            return m + n;
        }
        
        // dp[i][j]表示word1[:i]到word2[:j]的编辑距离
        int[][] dp = new int[m + 1][n + 1];
        // 初始化
        for (int i = 0; i <= m; i++) {
            dp[i][0] = i;
        }
        for (int j = 0; j <= n; j++) {
            dp[0][j] = j;
        }
        // 自底向上
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (word1.charAt(i - 1) == word2.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = 1 + Math.min(dp[i - 1][j - 1], Math.min(dp[i - 1][j], dp[i][j - 1]));
                }
            }
        }
        return dp[m][n];

    }
}
```