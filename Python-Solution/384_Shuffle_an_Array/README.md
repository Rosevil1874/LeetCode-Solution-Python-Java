# 384 - [打乱数组](https://leetcode.com/problems/shuffle-an-array/)


## 题解

```python
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        # 随机交换以打乱数组
        res = self.nums[:]
        for i in range(len(res)):
            j = random.randrange(i + 1)
            res[i], res[j] = res[j], res[i]
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
```
