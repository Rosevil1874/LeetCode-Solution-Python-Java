from collections import Counter
from functools import reduce 
class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """

        return list( reduce(Counter.__and__, map(Counter, A)).elements() )
            

A = ["bella","label","roller"]
# A = ["cool","lock","cook"]
# A = ["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"]
s = Solution()
r = s.commonChars(A)
print(r)
