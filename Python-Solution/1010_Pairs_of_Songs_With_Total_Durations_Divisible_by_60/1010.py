from collections import Counter
class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        count = 0
        c = Counter()

        for x in time:
        	count += c[ -x % 60 ]
        	c[ x % 60 ] += 1
        return count

        

# A = [30,20,150,100,40]
A = [60,60,60]
s = Solution()
r = s.numPairsDivisibleBy60(A)
print(r)
