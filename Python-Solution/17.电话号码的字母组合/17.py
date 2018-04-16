class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        begin = 0	#当前需要处理的digits的位置
        path = ''	#深搜路径
        res = []	#返回结果
        phone = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        self.deepSearch(digits, begin, path, res, phone)
        return res

    def deepSearch(self, digits, begin, path, res, phone):
    	# 深搜触底，回溯
    	if len(path) == len(digits) :
    		res.append(path)
    		return

    	# 遍历当前数字代表的所有字母
    	for char in phone[digits[begin]]:
    		path += char
    		# 从下一位开始到最后一位的组合情况
    		self.deepSearch(digits, begin + 1, path, res, phone)
    		path = path[:-1]


s = Solution()
r = s.letterCombinations('23')
print(r)