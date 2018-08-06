class Solution:
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        cnt , left, right = 0, -1 , -1
        for i in range(len(A)):
            if A[i] > R:
                left = i
            if A[i] >= L:
                right = i
            cnt += right - left
        return cnt
                

A = [2, 1, 4, 3]
L = 2
R = 3
s = Solution()
r = s.numSubarrayBoundedMax(A, L, R)
print(r)
    