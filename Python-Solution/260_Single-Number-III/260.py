class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 1. 将所有数字异或
        xor = 0
        for x in nums:
            xor ^= x

        # 2. 找出异或结果为1的一位（两个singlenumber在这一位上一个为0一个为1）
        mask = 1
        while (xor & mask == 0):
            mask <<= 1

        # 3. 分别找出两个single number（以上面找出的那一位为标准将两个single number分开到两组数中分别计算）
        a, b = 0, 0
        for x in nums:
            if x & mask:
                a ^= x
            else:
                b ^= x

        return [a,b]



        

nums = [1,2,1,3,2,5]

s = Solution()
r = s.singleNumber(nums)
print(r)