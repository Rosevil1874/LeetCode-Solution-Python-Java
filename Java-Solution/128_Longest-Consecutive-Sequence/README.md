# 128 - 最长连续序列

## 题解
**时间复杂度O(N)**
>参考StefanPochmann的[Simple O(n) with Explanation - Just walk each streak](https://leetcode.com/problems/longest-consecutive-sequence/discuss/41057/Simple-O(n)-with-Explanation-Just-walk-each-streak)

思路：  
1. 把数组装进set，这里的时间复杂度为O(N)，后面在set中查找就直接O(1)了；
2. 对集合set中的每个元素x，判断其是否为一个连续序列的开端(只要x-1不在集合中就是开端)；
3. 对每一个作为新序列开端的元素，依次查找x+1, x+2...是否在集合中，在的话就接在序列后，直到某个x+m不在集合中，说明序列断掉了，更新最长连续序列长度。

```java
class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int num: nums) {
            set.add(num);
        }

        int maxLen = 0;
        for (int num: set) {
            if (!set.contains(num - 1)) {
                int next = num + 1;
                while (set.contains(next)){
                    next++;
                }
                maxLen = Math.max(maxLen, next - num);
            }
        }
        return maxLen;
    }
}
```
