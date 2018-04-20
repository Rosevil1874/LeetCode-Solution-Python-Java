class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        if l <= 1:
            return s

        # dp[i][j]表示s[i..j]是回文串
        dp = [ [False] * l ] * l
        resLeft = resRight = 0
        dp[0][0] = True
        for i in range(1, l):
            dp[i][i] = True
            dp[i][i-1] = True

        for i in range(2, l + 1):       # 枚举子串长度，从2开始
            for j in range(0, l - i):   # 枚举子串起始位置
                if s[j] == s[j + i - 1] and dp[j + 1][j + i - 2]:
                    dp[j][j + i - 1] = True
                    if resRight - resLeft < i:
                        resLeft = j
                        resRight = j + i - 1
        return s[resLeft : resRight + 1 ]

solution = Solution()
r = solution.longestPalindrome("aaabaaaa")
print(r)
