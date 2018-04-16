class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        if l <= 1:
            return s

        start = 0
        max_len = 0
        max_s = ''
        for i in range(1, l):
            low = i - 1
            high = i
            while low>=0 and high<l and s[low]==s[high]:
                low -= 1
                high += 1
            if high-low+1 > max_len:
                max_len = high-low+1
                max_s = s[low+1 : high]

            low = i - 1
            high = i + 1
            while low>=0 and high<l and s[low]==s[high]:
                low -= 1
                high += 1
            if high-low+1 > max_len:
                max_len = high-low+1
                max_s = s[low+1 : high]
        return max_s
                    

solution = Solution()
r = solution.longestPalindrome("aaabaaaa")
print(r)
