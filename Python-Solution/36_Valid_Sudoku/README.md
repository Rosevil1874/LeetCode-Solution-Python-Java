# 36 - 有效的数独

## 题目描述
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

**Note:**
- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.
- The given board contain only digits 1-9 and the character '.'.
- The given board size is always 9x9.

## 题解一
老老实实地挨着判断三种情况。
```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return (self.is_row_valid(board) and self.is_col_valid(board) and self.is_square_valid(board))
    
    
    # 一个unit为一个能一维遍历的检查单位(一行或一列)
    def is_unit_valid(self, unit) -> bool:
        nums = [x for x in unit if x != '.']
        return len(set(nums)) == len(nums)
    
    
    # 检查每一个整行是否有效
    def is_row_valid(self, board) -> bool:
        for row in board:
            if not self.is_unit_valid(row):
                return False
        return True
    
    
    # 检查每一个整列是否有效
    def is_col_valid(self, board) -> bool:
        for col in zip(*board):
            if not self.is_unit_valid(col):
                return False
        return True
    
    
    # 检查每一个9X9的网格是否有效
    def is_square_valid(self, board) -> bool:
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.is_unit_valid(square):
                    return False
        return True
```

## 题解二
将三种判断条件地位置和值进行组合：
1. 行：将一行中每个值与其列索引组合，当有同样的组合出现，说明某一列中有重复值。如('8', 0), ('8', 0)
2. 列：将一列中每个值与其列索引组合，当有同样的组合出现，说明某一行中有重复值。
3. 九宫格：将九宫格中每个值与其行列索引组合，当有同样的组合出现，说明九宫格中有重复值。
```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        nums = []
        for i, row in enumerate(board):
            for j, x in enumerate(row):
                if x != '.':
                    nums += [(x, j), (i, x), (i//3, j//3, x)]
        return len(set(nums)) == len(nums)
```