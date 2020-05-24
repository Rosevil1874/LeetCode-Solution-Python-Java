# 75 - 分类颜色

## 题目描述
![problem](images/75.png)

## 题解

**思路**
1. 不管白色（1），把红色(0)和蓝色(2)移到对应位置就行；
2. 两个指针，red指向最后一个归位的红色，blue指向第一个归位的蓝色；
3. 遍历数组，每遇到一个红色就插入到red后面并更新指针位置，每遇到一个蓝色就插入到blue前面并更新blue指针位置。

```java
class Solution {
    public void sortColors(int[] nums) {
        int len = nums.length;
        int red = 0, blue = len - 1;

        int i = 0;
        while (i <= blue) {
            if (nums[i] == 0){
                swap(nums, i, red);
                red++;
            } else if (nums[i] == 2) {
                swap(nums, i, blue);
                blue--;
                i--; // 换到前面的数值是未经判断的，i-1会保持i的位置以检查此元素
            }
            i++;
            
        }
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}
```