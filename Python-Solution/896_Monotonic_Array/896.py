class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        length = len(A)
        if length < 2:
        	return True

        for i in range(length - 1):
        	sign = A[i] - A[i + 1]
        	if sign != 0:
        		break

        if i == length - 2:
        	return True
        elif sign > 0:
        	for j in range(i, length - 1):
        		if A[j] - A[j + 1] < 0:
        			return False
        	return True
        else:
        	for j in range(i, length - 1):
        		if A[j] - A[j + 1] > 0:
        			return False
        	return True
        
        	
   
# A = [1,2,2,3]
# A = [6,5,4,4]
# A = [1,3,2]
# A = [1,2,4,5]
# A = [1,1,1,1,1,1]
A = [1]
s = Solution()
r = s.isMonotonic(A)
print(r)
    