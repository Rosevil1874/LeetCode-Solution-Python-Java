class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return self.curr_min(word1, word2, 0, 0, {})
    
    
    def curr_min(self, word1, word2, i, j, memo):
        if i == len(word1) and j == len(word2):
            return 0
        elif i == len(word1):
            return len(word2) - j
        elif j == len(word2):
            return len(word1) - i
        
        if (i, j) not in memo:
            if word1[i] == word2[j]:
                cnt = self.curr_min(word1, word2, i + 1, j + 1, memo)
            else:
                insert = 1+ self.curr_min(word1, word2, i, j + 1, memo)
                delete = 1 + self.curr_min(word1, word2, i + 1, j, memo)    
                replace = 1 + self.curr_min(word1, word2, i + 1, j + 1, memo)    
                cnt = min(insert, delete, replace)
            memo[(i, j)] = cnt
        return memo[(i, j)]
        
    