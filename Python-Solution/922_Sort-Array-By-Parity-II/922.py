class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i, j = 0, 1
        length = len(A)
        while i < length and j < length:
        	if A[i]%2 == 0:
        		i += 2
        	elif A[j]%2 == 1:
        		j += 2
        	else:
        		A[i], A[j] = A[j], A[i]
        		i += 2
        		j += 2
        return A
        
# A = [3,1,2,4]
# A = [1,3,4,0]
A = [1,1,1,0,6,12]
# A = [1,0]
# A = [4,2,5,7]
s = Solution()
r = s.sortArrayByParity(A)
print(r)
    