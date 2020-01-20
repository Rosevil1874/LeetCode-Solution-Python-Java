class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)
        

# nums = [2,2,1]
nums = [4,1,2,1,2]

s = Solution()
r = s.singleNumber(nums)
print(r)