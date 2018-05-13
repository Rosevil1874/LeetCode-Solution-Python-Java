class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        cnt = i = 0
        while i < len(flowerbed) and cnt < n:
            if flowerbed[i] == 0:
                prev = 0 if (i == 0) else flowerbed[i - 1]
                next = 0 if (i == len(flowerbed) - 1) else flowerbed[i + 1]
                if prev == 0 and next == 0:
                    flowerbed[i] = 1
                    cnt += 1
            i += 1
        return cnt == n
        

flowerbed = [1,0,0,0,1,0,0]



n = 2  
s = Solution()
r = s.canPlaceFlowers(flowerbed, n)
print(r)