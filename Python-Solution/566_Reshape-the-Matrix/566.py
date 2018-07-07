import itertools
class Solution(object):
    def matrixReshape(self, nums, r, c):
	    if r * c != len(nums) * len(nums[0]):
	        return nums
	    it = itertools.chain(*nums)
	    return [list(itertools.islice(it, c)) for _ in range(r)]
        

                
       
nums = [[1,2,3,4]]
r = 2
c = 2
s = Solution()
r = s.matrixReshape(nums, r, c)
print(r)