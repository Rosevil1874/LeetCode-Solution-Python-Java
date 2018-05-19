class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = []
        n = 0
        maxSize = 0
        for i in range(len(nums)):
        	while i not in a:
        		a.append(i)
        		i = nums[i]
        		n += 1
        	maxSize = max(maxSize, n)
        	n = 0
        return maxSize
                
s = Solution()
res = s.arrayNesting([])  
print(res)