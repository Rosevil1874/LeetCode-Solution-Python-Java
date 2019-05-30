from functools import reduce
import operator
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(operator.xor, nums)
        

# nums = [2,2,1]
nums = [4,1,2,1,2]

s = Solution()
r = s.singleNumber(nums)
print(r)