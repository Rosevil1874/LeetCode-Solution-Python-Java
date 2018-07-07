class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ret = [0]
        for i in range(n):
            j = len(ret) - 1
            while j >= 0:
                ret.append(ret[j] | 1 << i)
                j -= 1
        return ret
        
                
s = Solution()
res = s.grayCode(1)  
print(res)