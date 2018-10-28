class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        diff = int( (sum(A) - sum(B))/2 )
        set_b = set(B)
        for x in set(A):
            target = x - diff
            if target in set_b:
                return ([x, target])
        	
        
A, B = [1,1], [2,2]
# A, B = [1,2], [2,3]
# A, B = [2], [1,3]
# A, B = [1,2,5], [2,4]
s = Solution()
r = s.fairCandySwap(A,B)
print(r)
    