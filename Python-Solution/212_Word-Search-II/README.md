# 212 - 单词搜索II
## 题目描述
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 
**Example:**

	Input: 
	board = [
	  ['o','a','a','n'],
	  ['e','t','a','e'],
	  ['i','h','k','r'],
	  ['i','f','l','v']
	]
	words = ["oath","pea","eat","rain"]

	Output: ["eat","oath"]
 

**Note:**

	All inputs are consist of lowercase letters a-z.
	The values of words are distinct.


>关联题目： 79. 单词搜索
知识点： [BFS & DFS](https://github.com/Rosevil1874/LeetCode/tree/master/Summary/BFS & DFS)， Trie-前缀树

## Trie树构建
1. 插入过程 对于一个单词，从根开始，沿着单词的各个字母所对应的树中的节点分支向下走，直到单词遍历完，将最后的节点标记为红色，表示该单词已插入Trie树。 
2. 查询过程 同样的，从根开始按照单词的字母顺序向下遍历trie树，一旦发现某个节点标记不存在或者单词遍历完成而最后的节点未标记为红色，则表示该单词不存在，若最后的节点标记为红色，表示该单词存在。

## DFS + 回溯 + Trie
显然，出自大神之手，Trie都是现学的༼༎ຶᴗ༎ຶ༽

**思路：**
1. 遍历矩阵，分别以每一个元素为起点开始深度遍历；
2. 若索引超出范围，返回False；
3. 若当前元素在Trie树中匹配，则将当前元素标记为已访问，并递归遍历矩阵中下一个（上下左右四个方向）元素，且向Trie树中下一个结点走一步，即往深处遍历；
4. 没有单词在以当前元素为起点的范围中代表不匹配，回溯（当前元素标记为未访问），选取下一个元素为起点DFS；
递归边界：走到Trie树的叶结点，代表此单词出现。

```python
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board:
            return False
        
        # 构建Trie树
        trie = {}
        for word in words:
            t = trie
            for c in word:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['#'] = '#'    # 单词存在于trie中的标记
            
        # for k, v in trie.items():
        #     print(k, v)
        
        # DFS
        self.res = set()
        self.visit = [[False] * len(board[0]) for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(trie, board, i, j, '')
        return list(self.res)
    
    
    def dfs(self, trie: dict, board:List[List[str]], i: int, j: int, pre: str) -> set:
        # 所有字母都存在, 加入结果中
        if '#' in trie:
            self.res.add(pre)
        
        # 越界，失败
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        
        # 未访问过此元素，且此元素存在于trie中
        if not self.visit[i][j] and board[i][j] in trie:
            tmp = board[i][j]           # 第一个字母匹配，接着判断剩下的
            self.visit[i][j] = True     # 代表已经访问过了
            self.dfs(trie[tmp], board, i + 1, j, pre + tmp)
            self.dfs(trie[tmp], board, i, j + 1, pre + tmp)
            self.dfs(trie[tmp], board, i - 1, j, pre + tmp)
            self.dfs(trie[tmp], board, i, j - 1, pre + tmp)
            self.visit[i][j] = False    # 回溯
```