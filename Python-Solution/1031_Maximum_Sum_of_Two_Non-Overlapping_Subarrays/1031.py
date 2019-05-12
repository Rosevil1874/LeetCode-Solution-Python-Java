class Solution(object):
    def maxSumTwoNoOverlap(self, A, L, M):
        """
        :type A: List[int]
        :type L: int
        :type M: int
        :rtype: int
        """
        for i in range(1, len(A)):
            A[i] += A[i - 1]
            res, Lmax, Mmax = A[L + M - 1], A[L - 1], A[M - 1]
            for i in range(L + M, len(A)):
                Lmax = max(Lmax, A[i - M]- A[i - L - M])
                Mmax = max(Mmax, A[i - L]- A[i - L - M])
                res = max(res, Lmax + A[i] - A[i - M], Mmax + A[i] - A[i - L])
        return res
                

        
# A = [0,6,5,2,2,5,1,9,4]
# L = 1
# M = 2

A = [3,8,1,3,2,1,8,9,0]
L = 3
M = 2

# A = [2,1,5,6,0,9,5,0,3,8]
# L = 4
# M = 3
s = Solution()
r = s.maxSumTwoNoOverlap(A, L, M)
print(r)
