class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        maxArea = area = 0

        left = 0
        right = n - 1
        res = 0
        maxLeft = maxRight = 0
        while left <= right:
            maxLeft = max(maxLeft, height[left])
            maxRight = max(maxRight, height[right])
            if maxLeft < maxRight:
                res += (maxLeft - height[left])
                left += 1
            else:
                res += (maxRight - height[right])
                right -= 1

        return res


heigh = [0,1,0,2,1,0,1,3,2,1,2,1]
s = Solution()
r = s.trap(heigh)
print(r)
