class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = len(nums)
        nums.sort()
        ret = []

        for i in range(l - 2):
            # 去重
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # 双指针归位！
            j, k = i + 1, l - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    ret.append( [nums[i], nums[j], nums[k]] )
                    j += 1
                    k -= 1

                    # 去重
                    while j < k and nums[j] == nums[j-1] :
                        j += 1
                    while j < k and nums[k] == nums[k+1] :
                        k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1

        return ret
        
        

s = Solution()
strs = [-1, 0, 1, 2, -1, -4]
res = s.threeSum(strs)
print(res)