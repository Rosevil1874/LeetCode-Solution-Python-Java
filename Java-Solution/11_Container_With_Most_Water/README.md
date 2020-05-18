# 11 - 盛最多水的容器


## 方法
思路【这个和CCF有一题‘最大的矩形’异曲同工啊】：
1. 要装最多水，就要矩形面积最大；
2. 以短边作为计算高度，木桶效应嘛( ･´ω\`･ )；
3. 从最大宽度开始，即双指针从两端向中间遍历；
4. 每次更新最大面积，指针相遇时返回结果。

```java
class Solution {
    public int maxArea(int[] height) {
        int curr_area = 0;
        int max_area = 0;
        int l = 0;
        int r = height.length - 1;

        while (l < r) {
            if (height[l] < height[r]) {
                curr_area = (height[l]) * (r - l);
                l++;
            } else {
                curr_area = (height[r]) * (r - l);
                r--;
            }
            max_area = Math.max(max_area, curr_area);
        }
        return max_area;
    }
}
```

