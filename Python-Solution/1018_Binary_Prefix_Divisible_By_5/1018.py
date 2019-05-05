class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        res = []
        num = 0
        for i, a in enumerate(A):
        	num = (num<<1 | a) % 5
        	res.append(num == 0)
        return res
                

        
# A = [0,1,1]
# A = [1,1,1]
A = [0,1,1,1,1,1]
# A = [1,1,1,0,1]
s = Solution()
r = s.prefixesDivBy5(A)
print(r)
