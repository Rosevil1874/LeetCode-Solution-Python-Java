class Solution:
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        for i in range(len(A)):
        	if abs(A[i] - i) > 1:
        		return False
        return True
        
# A = [1,0,2]
A = [1,2,0]
s = Solution()
r = s.isIdealPermutation(A)
print(r)
    