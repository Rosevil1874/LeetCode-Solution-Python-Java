class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        longest_len = 0
        left = -1
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                if not stack:
                    left = i
                else:
                    stack.pop(-1)
                    if not stack:
                        longest_len = max(longest_len, i - left)
                    else:
                        longest_len = max(longest_len, i - stack[-1])
        return longest_len
        
# string = ")()"
# string = ")()())"
# string = "())"
string = ")("
s = Solution()
res = s.longestValidParentheses(string)
print(res)

