class Solution:
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        lenA = len(A)
        if lenA <= 2:
            return False

        max_pos = A.index(max(A))
        if max_pos == 0 or max_pos == lenA - 1:
            return False

        left, right = A[0:max_pos], A[max_pos:lenA]
        if sorted(list(set(left))) == left and sorted(list(set(right))) == right[::-1]:  
            return True

        return False
        	
        
# A = [2,1]
# A = [3,5,5]
# A = [0,3,2,1]
# A = [1,7,9,5,4,1,2]
A = [4,20,32,45,49,45,31,21,20,16,11,8]
s = Solution()
r = s.validMountainArray(A)
print(r)
    