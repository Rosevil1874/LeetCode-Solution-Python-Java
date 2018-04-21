class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        i = 0
        while i < length:
            if nums[i] == val:
                del nums[i]
                length -= 1
            else:
                i += 1
        return nums
        # return length
        
nums = [0,1,2,2,3,0,4,2]
s = Solution()
r = s.removeElement(nums, 2)
for i in range(len(r)):
	print(r[i])
# print(r)