class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[x ^ 1 for x in row[::-1]] for row in A]

        
# A = [[1,1,0],[1,0,1],[0,0,0]]
A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]     
s = Solution()
r = s.flipAndInvertImage(A)
print(r) 