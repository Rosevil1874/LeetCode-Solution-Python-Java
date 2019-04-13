class Solution:
    def fib(self, N: int) -> int:
    	if N <= 1:
    		return N
    	else:
    		return self.fib(N - 1) + self.fib(N - 2)
        	      
       
N = 1
s = Solution()
r = s.fib(N)
print(r)
