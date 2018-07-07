class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = len(height)
        maxArea = 0
        area = 0
        i = 0
        j = l - 1

        while i < j:
            if height[i] < height[j]:
                h = height[i]
                area = (j - i) * h
                i += 1
            else:
                h = height[j]
                area = (j - i) * h
                j -= 1
            maxArea = max(maxArea, area)

        return maxArea
                
s = Solution()
res = s.maxArea([3,1,2,5,4])  
print(res)