# 42 - 接雨水


>审题：  
1. 面积计算；
2. 短板效应。

## 双指针

>思路：
1. 以逐个累计的方式替代长×宽的方式；
2. 从左往右记录一个最高点，若其右的值大于它，即为新的最高点，否则可以将其面积计入；
3. 从右往左记录一个最高点，若其左的值大于它，即为新的最高点，否则可以将其面积计入；
4. 左右指针相遇在最高点结束算法。

```java
class Solution {
    public int trap(int[] height) {
        int water = 0;
        int left = 0, right = height.length - 1;
        int leftMax = 0, rightMax = 0;

        while (left <= right) {
            if (height[left] <= height[right]) {
                if (height[left] < leftMax) {
                    water += (leftMax - height[left]);
                } else {
                    leftMax = height[left];
                }
                left++;
            } else {
                if (height[right] < rightMax) {
                    water += (rightMax - height[right]);
                } else {
                    rightMax = height[right];
                }
                right--;
            }
        }
        return water;
    }
}
```
