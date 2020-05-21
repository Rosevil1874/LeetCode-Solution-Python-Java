# 53 - 最大子序和


>审题：  
虽然题目没有明确说明最大和为负数时应该返回0还是这个负数，但是我用答案错误的代价试出来：**返回负数**

## 动态规划
1. sub problem: `maxSubArray(int A[], int i)`, means the maxSubArray for A[0:i] which must has A[i] as the end element;
2. If maxSubArray(A, i - 1) is negative, adding it to A[i] will only make a smaller sum, so we add only if it's non-negative;
3. DP function: `maxSubArray(A, i) = maxSubArray(A, i - 1) > 0 ? maxSubArray(A, i - 1) : 0 + A[i]`

用一个变量替代dp数组，节省空间开销：
```java
class Solution {
    public int maxSubArray(int[] nums) {
        int res = nums[0];
        int sum = 0;
        for (int num: nums) {
            sum = Math.max(sum + num, num);
            res = Math.max(res, sum);
        }
        return res;
    }
}
```
