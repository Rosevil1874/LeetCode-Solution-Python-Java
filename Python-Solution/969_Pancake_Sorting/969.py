class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = []
        for x in sorted(A)[::-1]:
        	index = A.index(x)
        	res.extend([index+1, x])
        	A = A[:index:-1] + A[:index]
        return res
        	
        
A = [3,2,4,1]
s = Solution()
r = s.pancakeSort(A)
print(r)
    