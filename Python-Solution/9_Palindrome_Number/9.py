class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False

        x = str(x)
        y = str(x)[::-1]
        return x == y

s = Solution()
res = s.isPalindrome(12321)
print(res)