def summaryRanges(self, nums):
    ranges = r = []
    for n in nums:
        if `n-1` not in r:
            r = []
            ranges += r,
        r[1:] = `n`,
    return map('->'.join, ranges)
        
       
nums = [0,2,3,4,6,8,9]
s = Solution()
r = s.summaryRanges(nums)
print(r)
