class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
        	return []
        ret = [[1]]
        for i in range(1, numRows):
        	ret.append( list( map(lambda x,y: x+y, ret[-1] + [0], [0] + ret[-1]) ) )
        return ret
        
        
        
s = Solution()
r = s.generate(5)
print(r)