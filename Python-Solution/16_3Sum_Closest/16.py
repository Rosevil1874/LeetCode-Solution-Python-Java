class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        min_diff = nums[0] + nums[1] + nums[2]
        the_sum = 0
        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1
            while j < k:
                val = nums[i] + nums[j] + nums[k]
                the_sum = val if abs(val - target) < abs(the_sum - target) else the_sum
                if val == target:
                    return target
                elif val < target:
                    j += 1
                else:
                    k -= 1
        return the_sum
        
        

s = Solution()
strs = [0,2,1,-3]

res = s.threeSumClosest(strs, 1)
print(res)