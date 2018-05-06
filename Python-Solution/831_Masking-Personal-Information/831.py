class Solution(object):
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        # 1. 首先判断是email还是phone
        if '@' in S:
            return self.maskEmail(S)
        else:
            return self.maskPhone(S)

    def maskEmail(self, S):
        # 1. 将所有字母转化成小写
        S = S.lower()

        # 2. mask name1
        idx = S.find('@')
        S = S[0] + '*****' + S[idx - 1 : ]

        return S

    def maskPhone(self, S):
        # 1. 去除特殊符号
        delete = '+-() '
        for c in delete:
            S = S.replace(c,'')
        
        # 2. 除最后四位以外都转化成‘*’
        if len(S) == 10:
            S = '***-***-' + S[-4:]
        else:
            S = '+' + '*' * (len(S) - 10) + '-***-***-' + S[-4:]

        return S

        
        
S = "86-(10)12345678"
s = Solution()
r = s.maskPII(S)
print(r) 