# 130 - [被围绕的区域](https://leetcode.com/problems/surrounded-regions/)

**题意：**把所有被'X'包围的'O'翻转成'X',在边上的'O'和不在边上但与边上的'O'相连的不算被包围。

## 题解
**思路：**  
1. 将所有和边相连的'O'替换成'T';
2. 将所有其他的'O'替换成'X', 把所有'T'替换回'O'。

```python
class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return 

        # 获取四条边上点的坐标
        m, n = len(board), len(board[0])
        queue = [x for y in range(max(m, n)) for x in ((0, y), (m - 1, y), (y, 0), (y, n - 1))]
        
        # BFS：依次检查边上是否为'O'
        while queue:
            i, j = queue.pop()
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'T'
                queue += (i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)

        # 将'O'替换成'X'，'T'替换回'O'
        for row in board:
            for i, c in enumerate(row):
                if c == 'O':
                    row[i] = 'X'
                elif c == 'T':
                    row[i] = 'O'
```
