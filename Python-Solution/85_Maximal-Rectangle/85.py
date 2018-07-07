class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
        	return 0

        col = len(matrix[0])
        height = [0] * (col + 1)
        maxArea = 0

        for row in matrix:
        	for i in range(col):
        		height[i] = height[i] + 1 if row[i] == '1' else 0

        	stack = [-1]
	        for i in range(len(height)):
	        	while height[i] < height[stack[-1]]:
	        		h = height[stack.pop()]
	        		w =i - 1 - stack[-1]
	        		maxArea = max(maxArea, w * h)
	        	stack.append(i)

        return maxArea

        
matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
s = Solution()
r = s.maximalRectangle(matrix)
print(r)     