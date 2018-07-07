class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        for i, val in nums:
            if val in d and i - d[val] <= k:
                return True
            d[val] = i
        return False
        
       
nums = [1,0,1,1]
s = Solution()
r = s.containsNearbyDuplicate(nums, 0)
print(r)
