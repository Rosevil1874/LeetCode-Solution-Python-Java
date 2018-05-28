class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        m, n = len(A), len(B)
        maxLen = float('-inf')
        c = [0 for i in range(n + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    c[j] = c[j - 1] + 1
                    maxLen = max(maxLen, c[j])
        return 0 if maxLen == float('-inf') else maxLen

solution = Solution()
A = [1,2,3,2,1]
B = [3,2,1,4,7]
res = solution.findLength(A, B)
print(res)