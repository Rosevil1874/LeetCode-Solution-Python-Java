class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 1, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            cnt = 0
            for i in nums:
                if i <= mid:
                    cnt += 1
            if cnt <= mid:
                left = mid + 1
            else:
                right = mid
        return left
            
        
# nums = [1,3,4,2,2]    
nums = [3,1,3,4,2]
s = Solution()
r = s.findDuplicate(nums)
print(r)