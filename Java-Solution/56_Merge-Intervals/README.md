# 56 - 合并区间


## 题解
思路：
1. 将intervals按区间的start升序排列；
2. 对interval中的每个区间，由于已经按start排序了，所以只需与前一个区间比较；
3. 若后一个区间的start小于等于前一个区间的end，说明两区间相交，合并时只需将end赋值为大的那一个即可。

```java
class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (v1, v2) -> v1[0]-v2[0]);

        int[][] res = new int[intervals.length][2];
        int idx = -1;
        for(int[] interval: intervals) {
            if (idx == -1 || interval[0] > res[idx][1]) {
                res[++idx] = interval;
            } else {
                res[idx][1] = Math.max(res[idx][1], interval[1]);
            }
        }
        return Arrays.copyOf(res, idx + 1);
    }
}
```
