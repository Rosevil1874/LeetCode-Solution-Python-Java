class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        the_sum = sum(A) // 3
        partition = 0

        s = 0
        for i in range(len(A)):
            s += A[i]
            if s == the_sum:
                partition += 1
                s = 0
                if partition == 2 and sum(A[i+1:]) == the_sum:
                    return True
        return False
                

        
A = [12,-4,16,-5,9,-3,3,8,0]
# A = [0,2,1,-6,6,-7,9,1,2,0,1]
# A = [0,2,1,-6,6,7,9,-1,2,0,1]
# A = [3,3,6,5,-2,2,5,1,-9,4]
# A = [18,12,-18,18,-19,-1,10,10]
s = Solution()
r = s.canThreePartsEqualSum(A)
print(r)
