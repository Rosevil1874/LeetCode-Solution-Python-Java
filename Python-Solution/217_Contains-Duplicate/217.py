class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0 or len(nums) == 1:
        	return False

        s = set()
        for i in range(len(nums)):
        	if nums[i] in s:
        		return True
        	s.add(nums[i])
        return False
        
       
nums = [1,1,1,3,3,4,3,2,4,2]
s = Solution()
r = s.containsDuplicate(nums)
print(r)
