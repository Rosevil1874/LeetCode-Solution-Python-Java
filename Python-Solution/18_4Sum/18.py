class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        nums = sorted(nums)
        l = len(nums)
        res = []

        # i1,i2,i3,i4为四个指针
        for i1 in range(0, l-3):
        	for i2 in range(i1 + 1, l-2):
        		i3 = i2 + 1
        		i4 = l - 1

        		# 循环结束条件为两指针相遇
        		while i3 < i4:
        			the_sum = nums[i1] + nums[i2] + nums[i3] + nums[i4]
        			if the_sum < target:
        				i3 += 1
        			elif the_sum > target:
        				i4 -= 1
        			else:
        				li = [ nums[i1], nums[i2], nums[i3], nums[i4] ] 
        				if li not in res:
        					res.append(li)
        				
        				i3 += 1

        return res


nums = [1, 0, -1, 0, -2, 2]
target = 0
s = Solution()
r = s.fourSum(nums, target)
print(r)
