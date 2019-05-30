class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones, twos = 0, 0
        for x in nums:
        	ones = (ones ^ x) & ~twos
        	twos = (twos ^ x) & ~ones
        return ones
        

nums = [2,2,3,2]
# nums = [0,1,0,1,0,1,99]

s = Solution()
r = s.singleNumber(nums)
print(r)