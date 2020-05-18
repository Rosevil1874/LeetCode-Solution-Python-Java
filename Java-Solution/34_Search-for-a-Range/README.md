# 34 - 搜索范围


## 二分查找

思路：使用两次二分查找，一次查找左边界，一次查找右边界。
1. 查找左边界range(0, len-1)：
    1. target > nums[mid]，第一个target在mid右边[left = mid + 1]；
    2. target < nums[mid], 第一个target在mid左边[right = mid]；
    3. target = nums[mid]，第一个target在mid左边[right = mid]。
    情况2,3中均需要将搜索范围往左边移动，所以可以合并。
2. 查找右边界range(left, len-1):
    1. target < nums[mid]，最后一个target在mid左边[right = mid - 1]；
    2. target > nums[mid], 最后一个target在mid右边[left = mid]；
    3. target = nums[mid]，最后一个target在mid右边或者target就在mid处[left = mid]。
    情况2,3中均需要将搜索范围往右边移动，所以可以合并。

```java
class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] targetRange = {-1, -1};
        int n = nums.length;
        if (n == 0) {
            return targetRange;
        }

        int l = 0, r = n - 1;
        // 查找左边界
        while(l < r) {
            int mid = l + (r - l)/2;
            if (target > nums[mid]) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }

        // target不存在
        if (nums[l] != target) {
            return targetRange;
        }

        // 查找右边界
        targetRange[0] = l;
        r = n - 1;
        while(l < r) {
            int mid = l + (r - l)/2 + 1; //令mid偏向右边
            if (target < nums[mid]) {
                r = mid - 1;
            } else {
                l = mid;
            }
        }
        targetRange[1] = r;
        return targetRange;
    }
}
```
