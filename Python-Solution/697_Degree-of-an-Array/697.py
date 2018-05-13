class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        firstAppear = {}    # 保存元素第一次出现的下标
        counter = {}        # 保存元素出现次数
        mostTime = 0        # 出现最多的次数
        subLen = 0          # 子数组长度
        for i, v in enumerate(nums):
            firstAppear.setdefault(v, i)    # 若字典中已经有此key的记录则保留，否则添加新的
            counter[v] = counter.get(v, 0) + 1
            if counter[v] > mostTime:
                mostTime = counter[v]
                subLen = i - firstAppear[v] + 1
            elif counter[v] == mostTime:
                subLen = min(subLen, i - firstAppear[v] + 1)
        return subLen

nums = [1,2,2,1,2,1,1,1,1,2,2,2]

      
s = Solution()
r = s.arrayPairSum(nums)
print(r)