class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        i = 0
        for n in nums:
        	if i < 2 or n > nums[i - 2]:
        		nums[i] = n
        		i += 1
        return i
        
nums = [0,0,1,1,1,1,2,3,3]
s = Solution()
r = s.removeDuplicates(nums)
# for i in range(len(r)):
# 	print(r[i])
print(r)