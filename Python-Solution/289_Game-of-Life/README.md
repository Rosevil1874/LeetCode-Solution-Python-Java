# 289 - 生命游戏

## 题目描述
![problem](images/289.png)

## 题解
恩，承认除了暴力想不到其他办法出来，但是我要把这个怪到“如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡”头上，为什么呀为什么呀，对我就是一直在思考它为什么会挂掉所以阻碍了思维，一定是这样( ･´ω\`･ )

用数字的比特位来表示状态，比如01表示初始为1，下一个状态为0。在矩阵中，初始状态只有0(00)和1(01)，他们的bit2均为0，我们只需判断他们在哪些情况下会变成1并标记。这个题解，我只能说，Amazing！

```python
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or len(board) == 0:
            return 
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                lives = self.live_neighbors(board, m, n, i, j)
        
                # 初始时bit2均为0，我们只关心它何时变为1
                if board[i][j] == 1 and lives >=2 and lives <= 3:
                    board[i][j] = 3     # 11
                if board[i][j] == 0 and lives == 3:
                    board[i][j] = 2     # 10
        
        # 将每个值右移一位，bit2为下一个状态
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1
                
    
    # 计算一个元素周围的live邻居数量
    def live_neighbors(self, board: List[List[int]], m:int, n: int, i: int, j: int):
        lives = 0
        # 计算九宫格内所有的1
        for x in range(max(0, i - 1), min(m - 1, i + 1) + 1):
            for y in range(max(0, j - 1), min(n - 1, j + 1) + 1):
                lives += board[x][y] & 1
        # 减掉中心的1
        lives -= board[i][j] & 1
        return lives
```
