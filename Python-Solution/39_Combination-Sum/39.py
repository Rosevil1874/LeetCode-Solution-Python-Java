class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        res = []
        candidates.sort()
        self.backtrack(res, [], candidates, target, 0)
        return res

    def backtrack(self, res, tmp, candidates, remain, start):
    	if remain < 0:
    		return
    	elif remain == 0:
    		res.append(tmp)
    	else:
    		for i in range(start, len(candidates)):
    			if candidates[i] > remain:		# 剪枝
    				break
    			# tmp.append(candidates[i])		# tmp按引用传递，直接这样append会导致最后res中的解全部是最后一个tmp的值
    			self.backtrack(res, tmp + [candidates[i]], candidates, remain - candidates[i], i) #可以重复使用同一元素，所以start是i而不是i+1

nums = [2,3,6,7]
s = Solution()
r = s.combinationSum(nums, 7)
print(r)
