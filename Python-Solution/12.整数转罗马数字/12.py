class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num <= 0:
            return ''

        ret = ''
        roman = ["M","CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        arab = [1000, 900, 500, 400, 100,90, 50, 40, 10, 9, 5, 4, 1]

        for i in range(13):
            if num > 0:
                if num < arab[i]:
                    continue
                while num >= arab[i]:
                    num -= arab[i]
                    ret += roman[i]
        return ret

s = Solution()
res = s.intToRoman(12321)
print(res)