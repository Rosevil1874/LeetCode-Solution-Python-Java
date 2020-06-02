# 152 - 乘积最大子序列

## 题解
要注意负数的情况。

```Java
class Solution {
    public int maxProduct(int[] nums) {
        int currMax = nums[0];
        int imin = nums[0], imax = nums[0];

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] < 0) {
                int temp = imax;
                imax = imin;
                imin = temp;
            }

            imax = Math.max(nums[i], imax*nums[i]);
            imin = Math.min(nums[i], imin*nums[i]);
            currMax = Math.max(currMax, imax);
        }
        return currMax;
    }
}
```
