class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        for i in range(len(A))[::-1]:
        	K, A[i] = divmod(A[i] + K, 10)

        return [int(i) for i in str(K)] + A if K else A
        # return list(map(int, str(K))) + A if K else A
        

# A, K = [1,2,0,0], 34
# A, K = [2,7,4], 181
A, K = [2,1,5], 806
# A, K = [9,9,9,9,9,9,9,9,9,9], 1
# A, K = [0], 23
s = Solution()
r = s.addToArrayForm(A, K)
print(r)
