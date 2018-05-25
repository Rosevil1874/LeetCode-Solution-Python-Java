class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if len(timeSeries) == 0:
        	return 0

        timeSeries.reverse()
        time = duration
        for i in range(1, len(timeSeries)):
        	diff = timeSeries[i - 1] - timeSeries[i]
        	if diff >= duration:
        		time += duration
        	else:
        		time += diff
        return time
        	      
       
timeSeries = [1,2]
duration = 2
s = Solution()
r = s.findPoisonedDuration(timeSeries, duration)
print(r)
