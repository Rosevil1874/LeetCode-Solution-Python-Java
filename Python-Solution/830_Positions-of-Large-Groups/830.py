class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        res = []
        i = 0
        while i < len(S):
        	j = i
        	while j < len(S) and S[i] == S[j]:
        		j += 1
        	if j - i >= 3:
        		res.append([i, j - 1])
        		i = j
        	else:
        		i += 1
        return res
        
S = "abbxxxxzzy"
s = Solution()
r = s.largeGroupPositions(S)
print(r) 