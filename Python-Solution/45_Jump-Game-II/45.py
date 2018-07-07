class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        last = 0
        then = 0
        count = 0
        for i in range(n):
            if then < i:
                count += 1
                then = last
            last = max(last, i + nums[i])
        return count
        

nums = [2,3,1,1,4]
# nums =  [2,3,0,1,4]
s = Solution()
r = s.canJump(nums)
print(r)
