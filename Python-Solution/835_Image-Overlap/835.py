import collections
class Solution:
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        ans = 0
        d = collections.defaultdict(int)
        a = []
        b = []
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    a.append((i, j))
                if B[i][j] == 1:
                    b.append((i, j))

        for aa in a:
            for bb in b:
                dd = (bb[0] - aa[0], bb[1] - aa[1])
                d[dd] += 1
                ans = max(ans, d[dd])
        return ans
        
        
A = [[1,1,0],
     [0,1,0],
     [0,1,0]]

B = [[0,0,0],
     [0,1,1],
     [0,0,1]]

s = Solution()
r = s.largestOverlap(A, B)
print(r)
   