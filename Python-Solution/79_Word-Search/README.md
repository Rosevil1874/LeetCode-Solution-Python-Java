# 79 - 单词搜索

## 题目描述
![problem](images/79.png)

>关联题目： [212. 单词搜索II](https://github.com/Rosevil1874/LeetCode/tree/master/Python-Solution/212_Word-Search-II)  
>知识点： [BFS & DFS](https://github.com/Rosevil1874/LeetCode/tree/master/Summary/BFS & DFS)

## DFS + 回溯
>虽然难度是中等，但是DFS也是好久没用过了，所以参考了一下别人的思路。

思路：
1. 遍历矩阵，分别以每一个元素为起点开始深度遍历；
2. 若索引超出范围或当前元素不匹配，返回False；
3. 若当前元素匹配，则将当前元素标记为已访问，并递归遍历矩阵中下一个（上下左右四个方向）元素，即往深处遍历；
4. 若某一元素不匹配，回溯（当前元素标记为未访问），选取下一个元素为起点DFS；
5. 递归边界：单词中所有字母均匹配。

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False
    
    
    def dfs(self, board: List[List[str]], i: int, j: int, word: str) -> bool:
        # 所有字母都存在且找到连续路径
        if len(word) == 0:  
            return True
        
        # 边界条件：1. 越界， 2. 值与路径中相应位置元素不相等， 3. 此位置已经走过
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[0]:
            return False
        
        # 此位置匹配但还未完全匹配path，向四个方向扩展判断, 任意方向上搜索到了结果都可返回True
        tmp = board[i][j]
        board[i][j] = '#'
        if self.dfs(board, i + 1, j, word[1:]) or self.dfs(board, i - 1, j, word[1:]) \
    or self.dfs(board, i, j + 1, word[1:]) or self.dfs(board, i, j - 1, word[1:]):
            return True
        
        # 回溯：此位置匹配但后面的位置都不匹配（没有返回True），将此位置恢复未访问状态，退回前一个位置
        board[i][j] = tmp
        return False
```
