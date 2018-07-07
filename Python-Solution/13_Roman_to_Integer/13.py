class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if s == '':
            return 0

        num = 0
        l = len(s)
        ref = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}

        for i in range(l):
            if i+1 >= l or ref[ s[i+1] ] <= ref[ s[i] ] :
                num += ref[s[i]]
            else:
                num -= ref[s[i]]
        return num

s = Solution()
res = s.romanToInt('VII')
print(res)