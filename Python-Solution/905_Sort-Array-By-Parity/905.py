class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        A.sort(key = lambda x: x%2)
        return A
        	
        
# A = [3,1,2,4]
# A = [1,3,5,0]
# A = [1,1,1,0,6,12]
# A = [0,1]
A = [5,0,3,8,6]
s = Solution()
r = s.sortArrayByParity(A)
print(r)
    