class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        # 环形旋转
        n = len(matrix)
        for i in range( n // 2 ):
            for j in range( i, n - i - 1 ):
                matrix[i][j], matrix[n-j-1][i], matrix[n-i-1][n-j-1], matrix[j][n-i-1] = \
                matrix[n-j-1][i], matrix[n-i-1][n-j-1], matrix[j][n-i-1], matrix[i][j]

       
        
matrix = [[1,2,3],[4,5,6],[7,8,9]]
s = Solution()
s.rotate(matrix)
for i in range(len(matrix)):
    print(matrix[i])
