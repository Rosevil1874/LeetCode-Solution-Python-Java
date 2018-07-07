class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
        	return s

        l = len(s)
        total = 2 * (numRows - 1)
        tmp = []
        ret = ''

        for k in range(numRows):
        	tmp.append('')

        for i in range(l):
        	idx = i % total
        	if idx >= numRows:
        		idx = total - idx
        	tmp[idx] += s[i]

        for j in range(numRows):
        	ret += tmp[j]
        return ret
                    

solution = Solution()
r = solution.convert("PAYPALISHI", 3)
print(r)
