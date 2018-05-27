class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        
        while left < right:
            print(left, right)
            if nums[left] < nums[right]:
                return nums[left]

            mid = (left + right) // 2
            if nums[left] < nums[mid]:
                left = mid
            elif nums[left] > nums[mid]:
                right = mid
            elif nums[left] == nums[mid]:
                left += 1

        return nums[left]
        

s = Solution()
nums =  [2,2,2,0,1]

res = s.findMin(nums)
print(res)