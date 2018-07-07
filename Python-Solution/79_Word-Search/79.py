class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        if not board:
            return False

        for i in range(len(board)):
        	for j in range(len(board[0])):
        		if self.DFS(board, i, j, word):
        			return True
        return False

    def DFS(self, board, i, j, word):
    	# 所有字母都存在
    	if len(word) == 0:
    		return True
    	if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
    		return False
    	tmp = board[i][j]		# 第一个字母匹配，接着判断剩下的
    	board[i][j] = '#'		# 代表以及访问过哦
    	if self.DFS(board, i + 1, j, word[1:]) or self.DFS(board, i - 1, j, word[1:]) or \
    		self.DFS(board, i, j + 1, word[1:]) or self.DFS(board, i, j - 1, word[1:]):
    		return True

    	board[i][j] = tmp		# 回溯
    	return False

    		
        
       
matrix = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

s = Solution()
r = s.exist(matrix, "SEE")
print(r)