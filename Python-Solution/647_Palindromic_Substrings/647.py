class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        cnt = 0
        
        for center in range(2*n - 1):
            left = center // 2
            right = center // 2 + center % 2
            while left >= 0 and right < n and s[left] == s[right]:
                cnt += 1
                left -= 1
                right += 1
        return cnt

        
string = 'abc'
s = Solution()
res = s.countSubstrings(string)
print(res)