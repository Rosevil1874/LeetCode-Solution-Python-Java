class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            pos = self.partition(nums, left, right)
            if pos > k - 1:          
                right = pos - 1
            elif pos < k - 1:
                left = pos + 1
            else:
                return nums[pos]
        
    # 返回第r小的元素，即第n-r大的元素
    def partition(self, nums, left, right):
        pivot = nums[left]
        l, r = left + 1, right
        while  l <= r:
            if nums[l] < pivot and nums[r] > pivot:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            elif nums[l] >= pivot:
                l += 1
            elif nums[r] <= pivot:
                r -= 1
        nums[left], nums[r] = nums[r], nums[left]
        return r
        
s = Solution()
nums = [1]
k = 1
res = s.findKthLargest(nums, k)
print(res)