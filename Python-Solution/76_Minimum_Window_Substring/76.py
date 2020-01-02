from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)   # 需要的每个字符及其个数
        missing = len(t)    # 还需要的字符个数
        
        i = I = J = 0       # 当前窗口s[i:j]，结果窗口s[I:J]
        for j, char in enumerate(s): # 令1作为遍历s的起始下标
            missing -= need[char] > 0
            need[char] -= 1
            
            # 需要的字符都凑齐了
            if not missing:
                # 当前window的s[i]个数多于需要的个数，则从窗口前开始删除多余的s[i]
                while i < j and need[s[i]] < 0: 
                    need[s[i]] += 1
                    i += 1
                # 更新结果子串的下标
                if not J or j - i <= J - I:
                    I, J = i, j
        return s[I:J+1]
        
       
# nums = [2,0,2,1,1,0]
S, T = "ADOBECODEBANC", "ABC"
s = Solution()
res = s.minWindow(S, T)
print(res)
