# 229 - 求众数II

## 题目描述
![problem](images/229.png)


>要求：  
1. 不使用除法；
2. 时间复杂度O(N)；
3. 进阶：空间复杂度O(1)。 

## 投票算法
思路：  
1. 从前往后遍历数组nums，对每个元素计算从第一个元素到除自身以外元素（nums0~(i-1))的积res[i]；
2. 从后往前遍历数组res，对每个元素res[i]依次乘上除nums[i]外后面元素的积就得到除自身以外的积。

**talk is cheap， look at the code ☟**

```python
class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [1 for i in range(n)]
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]

        right = 1
        i = n - 1
        while i >= 0:
            res[i] *= right
            right *= nums[i]
            i -= 1
        return res
```