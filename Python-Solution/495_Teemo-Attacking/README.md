# 268 - 提莫攻击

## 题目描述
![problem](images/268.png)

## 题解
思路：  
1. 先将数组反序，相当于从后往前判断；
2. 最后一次攻击肯定能持续duration时长，对于此前的每一次攻击都检查持续时间是否被后一次攻击打断：
	- 若被打断，则持续时间为两次攻击间隙；
	- 未被打断，则持续时间为duration。

```python
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
```