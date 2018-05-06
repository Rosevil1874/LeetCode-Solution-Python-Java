class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)	# 哨兵
        stack = [-1]
        maxReact = 0
        for i in range(len(heights)):
        	while heights[i] < heights[stack[-1]]:
        		h = heights[stack.pop()]
        		w = i - stack[-1] - 1
        		maxReact = max(maxReact, h *w)
        	stack.append(i)
        return maxReact
        
# heights = [2,1,5,6,2,3]
heights = [2,0,2]
s = Solution()
r = s.largestRectangleArea(heights)
print(r)     