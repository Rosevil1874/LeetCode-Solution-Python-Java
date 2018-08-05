import math
class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        n = len(seats)
        cnt, cntLeft, cntMid, cntRight = 0, 0, 0, 0

        # 最左端连续0子序列长度
        i = 0
        if seats[0] == 0:
            while i < n:
                if seats[i] == 0:
                    cntLeft += 1        
                else:
                    break
                i += 1
        res = cntLeft

        # 最右端连续0子序列长度
        j = n - 1
        if seats[n - 1] == 0:
            while j > 0:
                if seats[j] == 0:
                    cntRight += 1        
                else:
                    break
                j -= 1
        res = max(res, cntRight)

        # 中间连续0子序列长度
        while i < j:
            if seats[i] == 0:
                cnt += 1
            else:
                cntMid = max(cntMid, cnt)
                cnt = 0
            i += 1
        cntMid = max(cntMid, cnt)
        print(cntMid)

        res = max(res, math.floor((cntMid + 1) / 2))

        return res

# seats = [1,0,0,1,0,1,0,1]
# seats = [1,0,1]
# seats = [1,0,0,0,1,0,1]      
seats = [0,0,0,1]   
s = Solution()
r = s.maxDistToClosest(seats)
print(r)
    