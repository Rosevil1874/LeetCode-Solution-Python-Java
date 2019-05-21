from functools import reduce
class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        intersection = reduce(set.__and__, [set(d) for d in zip(A, B)] )
        if not intersection: 
        	return -1
        else:
        	x = intersection.pop()   # 就是你，幸运儿！
        	return  min(len(A) - A.count(x), len(B) - B.count(x))
            

A = [2,1,2,4,2,2]
B = [5,2,6,2,3,2]

# A = [3,5,1,2,3]
# B = [3,6,3,3,4]

s = Solution()
r = s.minDominoRotations(A, B)
print(r)
