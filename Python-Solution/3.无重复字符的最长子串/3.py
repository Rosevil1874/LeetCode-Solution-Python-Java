class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        l = len(s)
        if l == 0 or l == 1:
        	return l

        start = maxLength = 0
        usedChar = {}

        for i in range(l):
        	if s[i] in usedChar and start <= usedChar[s[i]]:
        		start = usedChar[s[i]] + 1
        	else:
        		maxLength = max(maxLength, i - start + 1)
        	usedChar[s[i]] = i
        return maxLength

solution = Solution()
r = solution.lengthOfLongestSubstring('loddktdji')
print(r)
