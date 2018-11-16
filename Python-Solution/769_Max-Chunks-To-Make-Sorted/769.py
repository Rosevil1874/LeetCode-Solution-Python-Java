class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        sortedArr = sorted(arr)
        i, cnt = 1, 0
        while i <= len(arr):
            while sorted(arr[:i]) != sortedArr[:i] and i <= len(arr):
                i += 1
            cnt += 1
            i += 1
        return cnt

        	
        
# arr = [4,3,2,1,0]
arr = [1,0,2,4,3]
# arr = [1,0,2,3,4]
s = Solution()
r = s.maxChunksToSorted(arr)
print(r)
    