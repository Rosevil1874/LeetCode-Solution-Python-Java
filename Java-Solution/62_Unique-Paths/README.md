# 62 - 不同路径


## 题解一
**时间复杂度：O(n^2)  
空间复杂度：O(m\*n)**

**思路**
1. 机器人每次只能向下或者向右移动一步，则当机器人到达某一点时有以下两种情况：
	1. 从上面的格子下来p[i - 1][j]；
	2. 从左边的格子过来p[i][j - 1]；
2. 由第一条得出状态方程：  
	1. p[i][j]: 机器人走到(i, j)处的路径条数；
	2. p[i][j] = p[i - 1][j] + p[i][j - 1]；
3. 边界条件为最左列和最上行不存在的情况，可以通过初始化p[0][j] = 1，p[i][0] = 1来处理，**注意是1不是0**。

```java
class Solution {
    public int uniquePaths(int m, int n) {
        int[][] dp = new int[m][n];
        for (int i = 0; i < m; i++) dp[i][0] = 1;
        for (int j = 0; j < n; j++) dp[0][j] = 1;
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            }
        }
        return dp[m - 1][n - 1];
    }
}
```


## 题解二
**时间复杂度：O(n^2)  
空间复杂度：O(m)**

**思路**
更新p[i][j]时只需要用到 p[i - 1][j] 和 p[i][j - 1]，所以只需要保存当前行和上一行的状态，而不是整个矩阵的状态。

```java
class Solution {
    public int uniquePaths(int m, int n) {
        int[] prev = new int[m];
        int[] curr = new int[m];
        Arrays.fill(prev, 1);
        Arrays.fill(curr, 1);

        for (int j = 1; j < n; j++) {
            for (int i = 1; i < m; i++) {
                curr[i] = curr[i - 1] + prev[i];
            }
            prev = curr;
        }
        return curr[m - 1];
    }
}
```


## 题解三

**思路：**  
可以看出题解二中的prev只是更新为了curr，所以连两个数组都用不上，用一个累加就行。缺点是代码可读性会差一点，分不清上一行和当前行。


```java
class Solution {
    public int uniquePaths(int m, int n) {
        int[] curr = new int[m];
        Arrays.fill(curr, 1);

        for (int j = 1; j < n; j++) {
            for (int i = 1; i < m; i++) {
                curr[i] += curr[i - 1];
            }
        }
        return curr[m - 1];
    }
}
```