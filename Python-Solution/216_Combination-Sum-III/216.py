class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        res = set()
        candidates = [1,2,3,4,5,6,7,8,9]
        self.backtrack(res, [], candidates, n, k, 0)
        return list( map(list, res) )

    def backtrack(self, res, tmp, candidates, remain, k, start):
    	if remain < 0 or k < 0:
    		return
    	elif remain == 0 and k == 0:
    		res.add(tuple(tmp))
    	else:
    		for i in range(start, len(candidates)):
    			if candidates[i] > remain:		# 剪枝
    				break
    			# tmp.append(candidates[i])		# tmp按引用传递，直接这样append会导致最后res中的解全部是最后一个tmp的值
    			self.backtrack(res, tmp + [candidates[i]], candidates, remain - candidates[i], k - 1, i+1) #不可以重复使用同一元素，start递增

s = Solution()
r = s.combinationSum3(3, 9)
print(r)
