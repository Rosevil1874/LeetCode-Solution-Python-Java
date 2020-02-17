class Solution:
    def mySqrt(self, x: int) -> int:
        res = 0
        bit = 1 << 16
        
        # 从高位向低位计算，看每一位上是否可以为1
        while bit > 0:
            res |= bit
            # res回退到前一个值
            if res > x // res:
                res ^= bit
            bit >>= 1
        return res

solution = Solution()
r = solution.mySqrt(8)
print(r)
