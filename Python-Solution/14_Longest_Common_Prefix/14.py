class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs_l = len(strs)
        if strs_l == 0:
            return ''

        pre = ''
        min_l = len(strs[0])
        for i in range(1, strs_l):
            min_l = min(min_l, len(strs[i]))

        for i in range(min_l):
            x = strs[0][i]
            for j in range(strs_l):
                if strs[j][i] != x :
                    return pre
            pre += x
        return pre
        

s = Solution()
strs = ['abcd','abcdef','abcdefggg']
res = s.longestCommonPrefix(strs)
print(res)