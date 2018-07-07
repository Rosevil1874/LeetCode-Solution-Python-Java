class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cnt = 0
        nums_set = set(nums)     #自动排序、去重
        if k < 0:
            return 0
        elif k == 0:
            for x in nums_set:
                if nums.count(x) > 1:
                    cnt += 1
        else:
            for x in nums_set:
                if x + k in nums_set:
                    cnt += 1
        return cnt


        
nums = [3, 1, 4, 1, 5]
s = Solution()
res = s.findPairs(nums, 2)
print(res)