class Solution:
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """

        
        
A = [[1,1,0],
     [0,1,0],
     [0,1,0]]

B = [[0,0,0],
     [0,1,1],
     [0,0,1]]

s = Solution()
r = s.transpose(A)
print(r)
   