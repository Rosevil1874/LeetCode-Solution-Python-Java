class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = j = 0
        while i < m + n and j < n:
            if nums2[j] <= nums1[i]:
                nums1.pop()
                nums1.insert(i, nums2[j])
                j += 1
            i += 1
            
        while j < n:
            i = m + j
            nums1[i] = nums2[j]
            i += 1
            j += 1
                    
            
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
s = Solution()
r = s.merge(nums1, m, nums2, n)
print(nums1)     