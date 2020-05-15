# 4 - 两个排序数组的中位数


## 二分查找
> cr:[两个排序数组的的中位数](https://zhuanlan.zhihu.com/p/33168674)

思路：
1. 中位数的性质: 在有序的有限数集中，在中位数左边的数的个数与右边的相等。
2. 这个问题可以进一步转化为在nums1数组抽前i个数在nums2数组中抽前j个数，且
`i+j == halflen, (halflen = (m+n+1)/2)`
（在奇数情况下左边的数比右边多一个）。
3. 二分查找i，通过等式得到
`j = halflen − i`，然后判断是否能满足中位数的条件。
4. 为了方便起见，同时减少运算次数，我们把数组size小的放到nums1，大的放到nums2，然后从nums1中查找i。
5. 进一步缩小查找范围，对于任意取的值i，我们能得到下面这张图中的关系。绿色的代表左边的数字，黄色的代表的是右边的数字。
![problem](images/idea.png)

```java
class Solution {
    public double findMedianSortedArrays(int[] A, int[] B) {
        int m = A.length;
        int n = B.length;
        // 根据数组大小交换顺序，小的在前
        if (m > n) {
            int[] temp1 = A; A = B; B = temp1;
            int temp2 = m; m = n; n = temp2;
        }

        int imin = 0, imax = m;     // A剩余部分的起止坐标
        int half_len = (m + n + 1) / 2;
        // 二分查找i值
        while (imin <= imax) {
            int i = (imin + imax) / 2;  // A剩余部分的中间位置
            int j = half_len - i;       // B中的j个数加上i刚好为合并序列的中间个数
            // i左边的数均在中位数左边，可排除
            if (i < imax && A[i] < B[j - 1]) {
                imin = i + 1;
            } 
            // i右边的数均在中位数右边，可排除
            else if (i > imin && A[i - 1] > B[j]){
                imax = i - 1;
            } 
            // i, j的值正好将两个数组分成在总数组中的两部分, 可以找出中位数了
            else {
                // 左边最大值
                int max_of_left = 0;
                if (i == 0) { max_of_left = B[j - 1]; }
                else if (j == 0) { max_of_left = A[i - 1]; }
                else { max_of_left = Math.max(A[i - 1], B[j - 1]); }

                // 奇数情况直接返回左边最大值
                if ((m + n) % 2 == 1) { return max_of_left; }

                // 右边最小值
                int min_of_right = 0;
                if (i == m) { min_of_right = B[j]; }
                else if (j == n) {min_of_right = A[i]; }
                else { min_of_right = Math.min(A[i], B[j]); }

                return (max_of_left + min_of_right) / 2.0;
            }
        }
        return 0.0;
    }
}
```