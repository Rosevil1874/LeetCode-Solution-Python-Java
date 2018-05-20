class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        minLen = triangle[-1]
        layer = len(triangle) - 2
        while layer >= 0:
            for i in range(layer + 1):
                minLen[i] = min(minLen[i], minLen[i + 1])+ triangle[layer][i]
            layer -= 1
        return minLen[0]

triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
# triangle = [[-1],[2,3],[1,-1,-3]]
s = Solution()
res = s.minimumTotal(triangle)
print (res)