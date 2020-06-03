# 198 - 打家劫舍


## 1. top-down recursive
小偷在一个房屋有两种选择，抢或不抢。抢劫房屋i的战利品是抢劫房屋i-2的最高战利品加上当前战利品，不抢房屋i的战利品是抢房屋i-1的最高战利品。 `loot(i) = Math.max( loot(i - 2) + currentHouseValue, loot(i - 1) )`

这个代码提交后的结果是Time Limit Exceeded。
```java
class Solution {
    private int loot(int[] nums, int i) {
        if (i < 0) {
            return 0;
        }
        return Math.max(nums[i] + loot(nums, i - 2), loot(nums, i - 1));
    }

    public int rob(int[] nums) {
        return loot(nums, nums.length - 1);
    }
}

```

## 2. bottom-up iterative + memo
计算下到下一户为止的最高战利品只需要用到前两户为止的最高战利品，因此不需要额外使用一个列表进行存储。
```Java
class Solution {
    public int rob(int[] nums) {
        if (nums == null || nums.length == 0){
            return 0;
        }

        int prev1 = 0;      // 到前1户为止的最高战利品
        int prev2 = 0;      // 到前2户为止的最高战利品
        for (int num: nums) {
            int temp = prev1;
            prev1 = Math.max(prev1, prev2 + num);
            prev2 = temp;
        }
        return prev1;
    }
}

```