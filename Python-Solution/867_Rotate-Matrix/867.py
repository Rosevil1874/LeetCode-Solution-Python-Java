class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(A)
        col = len(A[0])
        res = [[0] * row for i in range(col)]
        
        for i in range(row):
            for j in range(col):
                res[j][i] = A[i][j]
        return res
        
A = [[1,2,3],[4,5,6]]
s = Solution()
r = s.transpose(A)
print(r)
   