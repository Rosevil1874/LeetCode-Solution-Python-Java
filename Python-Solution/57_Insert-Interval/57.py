# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """

        n = len(intervals)
        overlap = 0         # 重叠区间数
        i = 0
        while i < n:
            # 1. 如果新区间的末尾小于当前区间的开头，则跳出循环
            if newInterval.end < intervals[i].start:
                break
            # 2. 如果新区间的开头大于当前区间的末尾，不作处理
            elif newInterval.start > intervals[i].end:
                pass
            # 3. 如果新区间和当前区间有重叠，合并区间
            else:
                newInterval.start = min(intervals[i].start, newInterval.start)
                newInterval.end = max(intervals[i].end, newInterval.end)
                overlap += 1
            i += 1

        # 如果有区间重叠，删除数组中所有与新区间重叠的区间
        if overlap > 0:
            intervals = intervals[:i-overlap] + intervals[i:]
        intervals.insert( i - overlap, newInterval)
        return intervals
            
        
        
intervals = []
tmp = Interval(1,3)
intervals.append(tmp)
tmp = Interval(6,9)
intervals.append(tmp)
# tmp = Interval(2,6)
# intervals.append(tmp)
# tmp = Interval(15,18)
# intervals.append(tmp)

newInterval = Interval(0, 1)

s = Solution()
r = s.insert(intervals, newInterval)
for i in range(len(r)):
	print(r[i].start, r[i].end)