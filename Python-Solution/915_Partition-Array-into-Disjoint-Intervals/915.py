class Solution:
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        left_max = A[0]
        all_max = left_max
        partition_index = 0
        for i in range(1, len(A)):
        	if left_max <= A[i]:
        		all_max = max( all_max, A[i] )
        	else:
        		left_max = all_max
        		partition_index = i
        return partition_index + 1
        	
        
A = [32,57,24,19,0,24,49,67,87,87]
# A = [1,1]
# A = [1,1,1,0,6,12]
# A = [5,0,3,8,6]
s = Solution()
r = s.partitionDisjoint(A)
print(r)
    