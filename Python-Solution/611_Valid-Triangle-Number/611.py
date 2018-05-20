class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        nums.sort()
        for i in range(2, len(nums)):
        	left, right = 0, i - 1
        	while left < right:
        		if nums[left] + nums[right] > nums[i]:
        			cnt += (right - left)
        			right -=1
        		else:
        			left += 1
        return cnt
        			
s = Solution()
res = s.triangleNumber([2,2,3,4])  
print(res)