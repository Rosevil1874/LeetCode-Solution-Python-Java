class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        res = []
        length = len(A)
        i, j = 0, length - 1
        while i <= j:
        	square_i = A[i] * A[i]
        	square_j = A[j] * A[j]
        	if square_i >= square_j:
        		res.insert(0, square_i)
        		i += 1
        	else:
        		res.insert(0, square_j)
        		j -= 1
        return res

       
A = [-4,-1,0,3,10]
# A = [-7,-3,2,3,11]
s = Solution()
r = s.fib(N)
print(r)
