class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        box = [-float('inf'), -float('inf'), -float('inf')]
        for x in nums:
            if x not in box:
                if x > box[0]:
                    box = [x, box[0], box[1]]
                elif x > box[1]:
                    box = [box[0], x, box[1]]
                elif x > box[2]:
                    box = [box[0], box[1], x]
        return box[0] if float('inf') in box else box[2]
        

        
        
s = Solution()
nums = [2, 2, 3, 1]
res = s.thirdMax(nums)
print(res)