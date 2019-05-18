class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        # 计算处于0左边的1，以及处于1右边的0的个数
        count1, flipCount = 0, 0
        for i in range(len(S)):
        	if S[i] == '0': 
        		if count1 == 0: continue
        		else: flipCount += 1
        	else:
        		count1 += 1
        	flipCount = min(flipCount, count1)
        	
        return flipCount
        
        
# S = "00110"
# S = "010110"
# S = "00011000"
# S = "0101100011"   # 3
S = "10011111110010111011"   # 5

s = Solution()
r = s.minFlipsMonoIncr(S)
print(r)
    