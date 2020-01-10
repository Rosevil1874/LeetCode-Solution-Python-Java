from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        n = len(p)
        win_p, win_s = defaultdict(int), defaultdict(int)
        for x in p:
            win_p[x] += 1
        for x in s[:n-1]:
            win_s[x] += 1
        
        for i in range(len(s) - n + 1):
            win_s[s[i + n - 1]] += 1    # 窗口加上最右值
            if win_s == win_p:
                res.append(i)
            win_s[s[i]] -= 1    # 窗口向右滑动，去掉最左值
            if not win_s[s[i]]:
                del win_s[s[i]]
        return res
        
nums = [4,3,2,7,8,2,3,1]
s = Solution()
res = s.findDuplicates(nums)
print(res)