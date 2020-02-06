class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        
        stack, num, sign = [], 0, '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = num*10 + int(s[i])
            if s[i] in '+-*/' or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop()*num)
                else:
                    pre = stack.pop()
                    if pre < 0:
                        stack.append(-(abs(pre)//num))
                    else:
                        stack.append(pre//num)
                sign = s[i]
                num = 0
        return sum(stack)

solution = Solution()
s = "3+2*2"
print(solution.calculate(s))