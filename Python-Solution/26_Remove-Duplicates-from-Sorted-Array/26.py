class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        newLen = length
        i = 1
        while i < length:
        	if nums[i] == nums[i-1]:
        		del nums[i]
        		length -= 1
        	else:
        		i += 1
        return nums
        # return length
        
nums = [0,0,1,1,1,2,2,3,3,4]
s = Solution()
r = s.removeDuplicates(nums)
for i in range(len(r)):
	print(r[i])
# print(r)