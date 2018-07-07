class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        res = []
        self.helper( '', res, n, 0, 0)
        return res

    def helper(self, curr, res, n, left, right):
    	# 当 右括号 = n 时已经找到一个结果
    	if right == n:
    		res.append(curr)
    	if left < n:
    		self.helper(curr+'(',res, n, left+1, right)
    	if left > right:
    		self.helper(curr+')',res, n, left, right+1)

s = Solution()
r = s.generateParenthesis(3)
print(r)