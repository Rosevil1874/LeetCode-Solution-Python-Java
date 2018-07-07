class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0:
            return False

        d = {}
        w = t + 1           # 桶的容量
        for i, val in enumerate(nums):
            n = val // w    # 分配到第n个桶
            
            # 1. 当前元素与之前出现过的某元素在同一个桶内，则其值之差不大于t
            if n in d:      
                return True

            # 2. 当前元素在之前出现过的某元素的前一个桶内，则需判断其值之差是否不大于t
            if n - 1 in d and abs(val - d[n - 1]) < w :
                return True
            
            # 3. 当前元素在之前出现过的某元素的后一个桶内，则需判断其值之差是否不大于t
            if n + 1 in d and abs(val - d[n + 1]) < w :
                return True

            # 将元素放入相应桶内
            d[n] = val

            # 删除桶中索引之差超过k的元素
            if i >= k:
                del d[nums[i - k] // w]

        return False
        
       
nums = [4,2]
s = Solution()
r = s.containsNearbyAlmostDuplicate(nums, 2, 1)
print(r)
