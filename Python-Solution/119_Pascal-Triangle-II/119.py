class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ret = [1]
        for i in range(1, rowIndex + 1):
            ret = list( map(lambda x,y: x + y, [0] + ret, ret + [0]) )
        return ret
        
s = Solution()
r = s.getRow(0)
print(r)