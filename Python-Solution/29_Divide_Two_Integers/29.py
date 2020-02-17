class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 符号位
        is_positive = (dividend < 0) == (divisor < 0)
        
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                temp <<= 1
                i <<= 1

        # 恢复符号
        if not is_positive:
            res = -res

        # 检查溢出
        if res > 2**31 - 1:
            return 2**31 - 1
        elif res < -2**31:
            return -2**31
        else:
            return res



solution = Solution()
r = solution.divide(7, -3)
print(r)
