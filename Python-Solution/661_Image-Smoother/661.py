from copy import deepcopy

class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(M)
        col = len(M[0]) if row else 0
        res = deepcopy(M)
        for x in range(row):
            for y in range(col):
                neighbors = [
                    M[_x][_y]
                    for _x in (x-1, x, x+1)
                    for _y in (y-1, y, y+1)
                    if 0 <= _x < row and 0 <= _y < col
                ]
                res[x][y] = sum(neighbors) // len(neighbors)
        return res
        

nums = [
 [1,1,1],
 [1,0,1],
 [1,1,1]]
s = Solution()
r = s.imageSmoother(nums)
print(r)