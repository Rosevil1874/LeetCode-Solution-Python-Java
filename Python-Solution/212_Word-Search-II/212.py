class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        
        if not board:
            return False

        # 构建Trie树
        trie = {}
        for w in words:
            t = trie
            for c in w:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['#'] = '#'

        for k, v in trie.items():
            print(k, v)

        # DFS
        self.res = set()
        self.visited = [ [False] * len(board[0]) for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.DFS(board, i, j, trie, '')
        return list(self.res)

    def DFS(self, board, i, j, trie, pre):
        # 走到了Trie树的叶结点，则此单词存在
        if '#' in trie:
            self.res.add(pre)
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
            
        if not self.visited[i][j] and board[i][j] in trie:
           tmp = board[i][j]               # 第一个字母匹配，接着判断剩下的
           self.visited[i][j] = True       # 代表已经访问过哦
           self.DFS(board, i + 1, j, trie[tmp], pre + tmp) 
           self.DFS(board, i - 1, j, trie[tmp], pre + tmp)
           self.DFS(board, i, j + 1, trie[tmp], pre + tmp) 
           self.DFS(board, i, j - 1, trie[tmp], pre + tmp)
           self.visited[i][j] = False       # 回溯

            
        
words = ["oath","pea","eat","rain"]      
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]


s = Solution()
r = s.findWords(board, words)
print(r)