
class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []

        for x in nums:
        	idx = abs(x) - 1
        	if nums[idx] < 0:
        		res.append(idx + 1)
        	nums[idx] = - nums[idx]

        return res
        
nums = [4,3,2,7,8,2,3,1]
s = Solution()
res = s.findDuplicates(nums)
print(res)