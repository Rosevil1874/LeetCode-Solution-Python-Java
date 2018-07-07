class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return 0

        n = len(digits)
        if digits[n - 1] != 9:
            digits[n - 1] += 1
        else:
            i = n - 1
            while digits[i] == 9:
                digits[i] = 0
                i -= 1
            if i >= 0:
                digits[i] += 1
            else:
                digits.insert(0, 1)

        return digits

        
       
digits = [9]
s = Solution()
r = s.plusOne(digits)
print(r)
