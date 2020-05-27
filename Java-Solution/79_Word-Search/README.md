# 79 - 单词搜索


## DFS + 回溯
>虽然难度是中等，但是DFS也是好久没用过了，所以参考了一下别人的思路。

思路：
1. 遍历矩阵，分别以每一个元素为起点开始深度遍历；
2. 若索引超出范围或当前元素不匹配，返回False；
3. 若当前元素匹配，则将当前元素标记为已访问，并递归遍历矩阵中下一个（上下左右四个方向）元素，即往深处遍历；
4. 若某一元素不匹配，回溯（当前元素标记为未访问），选取下一个元素为起点DFS；
5. 递归边界：单词中所有字母均匹配。

```java
class Solution {
    public boolean exist(char[][] board, String word) {
        int m = board.length;
        if (m == 0) {
            return false;
        }
        int n = board[0].length;

        for(int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (backtrack(i, j, board, word)) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean backtrack(int i, int j, char[][] board, String word) {
        // 匹配整个字符串
        if (word.length() == 0) {
            return true;
        }
        // 超出边界或当前字符与字符串中当前字符不匹配
        if (i < 0 || i >= board.length || j < 0 || j >= board[0].length || board[i][j] != word.charAt(0)) {
            return false;
        }

        // DFS
        char temp = board[i][j];
        board[i][j] = '#';      // 标记保证不重复使用
        String remain = word.substring(1);
        if (backtrack(i + 1, j, board, remain) || backtrack(i, j + 1, board, remain) || backtrack (i - 1, j, board, remain) || backtrack(i, j - 1, board, remain)) {
            return true;
        }

        // 回溯
        board[i][j] = temp;
        return false;
    }
}
```
