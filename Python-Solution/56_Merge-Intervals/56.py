# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort( key=lambda i: i.start)

        i = 0
        while i < (len(intervals) - 1):
        	j = i + 1
        	if intervals[j].start <= intervals[i].end:
        		intervals[i].end = max(intervals[i].end, intervals[j].end)
        		del intervals[j]
        	else:
        		i += 1

        return intervals
        
intervals = []
tmp = Interval(1,3)
intervals.append(tmp)
tmp = Interval(8,10)
intervals.append(tmp)
tmp = Interval(2,6)
intervals.append(tmp)
tmp = Interval(15,18)
intervals.append(tmp)

s = Solution()
r = s.merge(intervals)
for i in range(len(r)):
	print(r[i].start, r[i].end)