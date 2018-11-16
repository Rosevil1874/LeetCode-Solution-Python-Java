from collections import Counter
class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        sortedArr = sorted(arr)
        cnt, c1, c2 = 0, Counter(), Counter()
        for a, b in zip(arr, sorted(arr)):
            c1[a] += 1
            c2[b] += 1
            cnt += c1 == c2
        return cnt

        	
        
# arr = [5,4,3,2,1]
# arr = [2,1,3,4,4]
arr = [2,1,3,6,6,5,4,4]
s = Solution()
r = s.maxChunksToSorted(arr)
print(r)
    