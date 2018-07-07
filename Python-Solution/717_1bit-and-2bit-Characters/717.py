class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(bits):
        	if i == len(bits) - 1:
        		return True
        	elif bits[i] == 1:
        		i += 2
        	else:
        		i += 1
        return False
                
s = Solution()
res = s.isOneBitCharacter([ 0])  
print(res)