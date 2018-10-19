from collections import Counter
from functools import reduce
class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        def gcd(a, b):
        	while b:
        		a, b = b, a%b
        	return a

        cnt = Counter(deck).values()
        return reduce(gcd, cnt) >= 2
        	
        
# deck = [1,2,3,4,4,3,2,1]
deck = [1,1,1,2,2,2,3,3]
# deck = [1]
# deck = [1,1]
# deck = [1,1,2,2,2,2]
s = Solution()
r = s.hasGroupsSizeX(deck)
print(r)
    