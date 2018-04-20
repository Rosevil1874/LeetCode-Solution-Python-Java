class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        s_len = len(s)
        p_len = len(p)
        
        # dp[0][0]为True，其他均为False（两个空数组match）
        dp = [[True] + [False] * s_len]
        for i in range(p_len):
            dp.append([False]*(s_len+1))

        for i in range(1, p_len + 1):
            x = p[i-1]
            if x == '*' and i > 1:
                dp[i][0] = dp[i-2][0]
            for j in range(1, s_len+1):
                if x == '*':
                    dp[i][j] = dp[i-2][j] or dp[i-1][j] or (dp[i-1][j-1] and p[i-2] == s[j-1]) or (dp[i][j-1] and p[i-2]=='.')
                elif x == '.' or x == s[j-1]:
                    dp[i][j] = dp[i-1][j-1]

        return dp[p_len][s_len]
            

s = Solution()
res = s.isMatch("mississippi", "mis*is*p*.")  
print(res)