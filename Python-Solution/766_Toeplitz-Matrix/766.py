class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        return all(matrix[i][:-1] == matrix[i+1][1:] for i in range(len(matrix) - 1))
            
       
# matrix = [
# [1,2,3,4],
# [5,1,2,3],
# [9,5,1,2]
# ]
matrix = [[1,2],[2,2]]
# matrix = [[18],[66]]
s = Solution()
r = s.isToeplitzMatrix(matrix)
print(r)