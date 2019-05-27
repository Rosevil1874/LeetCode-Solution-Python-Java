class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
        	return '0'

        product = [0] * (len(num1) + len(num2))
        pos = len(product) - 1
        for a in reversed(num1):
        	tempPos = pos
        	for b in reversed(num2):
        		product[tempPos] += int(a) * int(b)
        		product[tempPos - 1] += product[tempPos]//10
        		product[tempPos] %= 10
        		tempPos -= 1
        	pos -= 1

        pt = 0
        while pt < len(product) - 1 and product[pt] == 0:
        	pt += 1

        return ''.join(map(str, product[pt:]))


num1, num2 = '2', '3'
# num1, num2 = '123', '456'
s = Solution()
r = s.multiply(num1, num2)
print(r)
