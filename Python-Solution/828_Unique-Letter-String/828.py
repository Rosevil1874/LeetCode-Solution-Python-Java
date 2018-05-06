class Solution(object):
    def uniqueLetterString(self, S):
        """
        :type S: str
        :rtype: int
        """
        ret = 0
        for i in range(len(S)):
            left = i - 1
            right = i + 1
            while left >= 0 and S[left] != S[i]:
                left -= 1
            while right < len(S) and S[right] != S[i]:
                right += 1
            ret += (right - i) * (i - left)
        return ret % (1000000007)

S = "abc"
s = Solution()
print( s.uniqueLetterString(S) )
