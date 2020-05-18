# 31 - 下一个排列


>审题：
1. 原地操作，无返回值；
2. 常数额外空间。
3. 可以这样理解：输入一个整数数组，该数组按照下标顺序代表一个整数，如[1,2,3]代表123，找出以这个数组元素为数位的，比当前这个数字大的数中的最小值，若当前已经是最大值，则输出最小值（升序）。

## 全排列
集合{ 1,2,3}的全排列为：
- { 1 2 3 }
- { 1 3 2 }
- { 2 1 3 }
- { 2 3 1 }
- { 3 2 1 }
- { 3 1 2 }


## 题解
思路：
1. 从后往前遍历，倒数第二位开始，找到可以替换的最小值x；
2. 从后往前找一个比当前值大的数中的最小值，与x进行替换；
3. 替换后保证后续序列为升序（最小）。

```java
class Solution {
    public void nextPermutation(int[] nums) {
        // 从后往前找到第一个可以交换的值（小于其后元素的值）
        int i = nums.length - 2;
        while (i >= 0 && nums[i] >= nums[i +1]){
            i--;
        }

        // 从后往前找到第一个大于x的最小值进行交换
        if (i >= 0) {
            int j = nums.length - 1;
            while (j >= 0 && nums[j] <= nums[i]){
                j--;
            }
            swap(nums, i, j);
        }
        reverse(nums, i + 1);
    }

    // 翻转数组后半段
    private void reverse(int[] nums, int start) {
        int i = start, j = nums.length - 1;
        while (i < j) {
            swap(nums, i, j);
            i++;
            j--;
        }
    }

    // 交换数组元素
    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}
```