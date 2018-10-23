# -*- coding: utf-8 -*-
# 给定 nums = [2, 7, 11, 15], target = 9

# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]

nums = [2, 7, 11, 15]
target = 9

class Solution:
    def twoSum(self, nums, target):
    	tmp = {}
    	for i, a in enumerate(nums):
    	    if target-a in tmp:
    	        return (tmp[target-a], i)
    	    else:
    	        tmp[a] = i

s = Solution()
res = s.twoSum(nums, target)
print (res)