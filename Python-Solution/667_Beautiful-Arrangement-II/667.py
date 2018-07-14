class Solution:
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        l, r = 1, n
        res = []
        while l <= r:
            if k > 1:
                if k % 2 == 1:
                    res.append(l)
                    l += 1
                else:
                    res.append(r)
                    r -= 1
            else:
                res.append(l)
                l += 1
            k -= 1
        return res

n, k = 5, 3     
s = Solution()
res = s.constructArray(n, k)
print(res)