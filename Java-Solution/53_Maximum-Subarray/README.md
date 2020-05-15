# 53 - 最大子序和

## 题目描述
![problem](images/53.png)

>审题：  
虽然题目没有明确说明最大和为负数时应该返回0还是这个负数，但是我用答案错误的代价试出来：**返回负数**

## 动态规划
>cr: [DP-solution-and-some-thoughts](https://leetcode.com/problems/maximum-subarray/discuss/20193/DP-solution-and-some-thoughts)

1. sub problem: `maxSubArray(int A[], int i)`, means the maxSubArray for A[0:i] which must has A[i] as the end element;
2. If maxSubArray(A, i - 1) is negative, adding it to A[i] will only make a smaller sum, so we add only if it's non-negative;
3. DP function: `maxSubArray(A, i) = maxSubArray(A, i - 1) > 0 ? maxSubArray(A, i - 1) : 0 + A[i]`

>Runtime: 68 ms, faster than 81.02% of Python3 online submissions.  
Memory Usage: 13.6 MB, less than 70.73% of Python3 online submissions.

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        max_sum = nums[0]
        
        for i in range(1,n):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            max_sum = max(max_sum, dp[i])
        return max_sum
```

用一个变量替代dp数组，节省空间开销：
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        curr_sum = nums[0]
        max_sum = nums[0]
        
        for i in range(1,n):
            curr_sum = max(curr_sum + nums[i], nums[i])
            max_sum = max(max_sum, curr_sum)
        return max_sum
```

再简化：每一个nums[i]的值都表示，截止到目前为止，前面所有可能的countinuous array的最大的和。
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)
```


## 分治法
**时间复杂度O(n * log n)**

思路：
1. 把序列二分之后，最大子序列的存在有以下三种情况：
	1. 在左子序列；
	2. 在右子序列；
	3. 一部分在左子序列右边，一部分在右子序列左边。
2. 对于情况1,2可递归求得；
3. 对于情况三可求得左子序列从后往前最大子序列s1，右子序列从前往后最大子序列s2，最优值即为s1 + s2.

```python
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return self.maxSubSum(nums, 0, n - 1)

    def maxSubSum(self, nums, left, right):
    	# base case
    	if left == right:
    		# if nums[left] > 0:
    		return nums[left]
    		# else:
    			# return 0

    	mid = (left + right) // 2
    	maxLeftSum = self.maxSubSum(nums, left, mid)
    	maxRightSum = self.maxSubSum(nums, mid + 1, right)

    	# 求跨边界最优值的左右子序列
    	# maxLeftBorderSum = maxRightBorderSum = 0	
    	# leftBorderSum = rightBorderSum = 0

    	maxLeftBorderSum = leftBorderSum = nums[mid]
    	i = mid - 1
    	while i >= left:
    		leftBorderSum += nums[i]
    		maxLeftBorderSum = max(maxLeftBorderSum, leftBorderSum)
    		i -= 1

    	maxRightBorderSum = rightBorderSum = nums[mid + 1]
    	i = mid + 2
    	while i <= right:
    		rightBorderSum += nums[i]
    		maxRightBorderSum = max(maxRightBorderSum, rightBorderSum)
    		i += 1

    	maxBorderSum = maxLeftBorderSum + maxRightBorderSum

    	return max(maxLeftSum, maxRightSum, maxBorderSum)
```