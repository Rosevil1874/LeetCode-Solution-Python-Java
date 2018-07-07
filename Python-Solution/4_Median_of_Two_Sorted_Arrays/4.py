class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)

        # 根据数组大小交换顺序，小的在前
        if m > n:
        	tmpn = m
        	m = n
        	n = tmpn
        	tmparr = nums1
        	nums1 = nums2
        	nums2 = tmparr

        imin = 0
        imax = m
        half_len = (m + n + 1)//2

        # 二分查找i值
        while imin <= imax:
        	i = (imin + imax) // 2
        	j = half_len - i
        	if i < m and nums2[j - 1] > nums1[i] :
        		imin = i + 1
        	elif i > 0 and nums1[i - 1] > nums2[j] :
        		imax = i - 1
        	else:
        		# 左边最大值
        		if not i:
        			max_of_left = nums2[j-1]
        		elif not j:
        			max_of_left = nums1[i-1]
        		else:
        			max_of_left = max(nums1[i-1], nums2[j-1])
        		# 如果总为奇数直接返回左边最大值
        		if (m + n)%2 == 1:
        			return max_of_left
        		# 右边最小值
        		if i == m:
        			min_of_right = nums2[j]
        		elif j == n:
        			min_of_right = nums1[i]
        		else:
        			min_of_right = min(nums1[i], nums2[j])
        		return (max_of_left + min_of_right) / 2
        return 0


nums1 = [1, 2]
nums2 = [3, 4]
solution = Solution()
r = solution.findMedianSortedArrays(nums1, nums2)
print(r)
