class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        cnt1, cnt2, candidate1, candidate2 = 0, 0, 0, 1
        for val in nums:
            if val == candidate1:
                cnt1 += 1
            elif val == candidate2:
                cnt2 += 1
            elif cnt1 == 0:
                candidate1, cnt1 = val, 1
            elif cnt2 == 0:
                candidate2, cnt2 = val, 1
            else:
                cnt1, cnt2 = cnt1 - 1, cnt2 - 1
        return [x for x in (candidate1, candidate2) if nums.count(x) > len(nums)//3]

nums = [1,1,1,3,3,2,2,2]

s = Solution()
r = s.majorityElement(nums)
print(r)