# 76 - 最小覆盖子串

## 题目描述
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

**Example:**

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

**Note:**
If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.


## 题解

```java
class Solution {
    public String minWindow(String s, String t) {
        if (s == null || t == null || s.length() == 0 || t.length() == 0) {
            return "";
        }

        // 频数数组：t中每个字符出现的频数
        int[] need = new int[128];
        for (char c: t.toCharArray()) {
            need[c]++;
        }

        int start = 0, end = 0;     // 字串的起止位置
        int left = 0, right = 0;    // 左右指针坐标
        int match = 0;              // 匹配的字符个数
        int minLen = s.length() + 1;

        while (right < s.length()) {
            char charRight = s.charAt(right);
            need[charRight]--;
            if (need[charRight] >= 0) { // 匹配到了t中的一个字符
                match++;
            }
            right++;

            // 窗口内包含了t中每个字符时，左边界收缩
            while (match == t.length()) {
                int len = right - left;
                if (len < minLen) {
                    minLen = len;
                    start = left;
                    end = right;
                }
                // 左边界收缩
                char charLeft = s.charAt(left);
                need[charLeft]++;
                if (need[charLeft] > 0) {
                    match--;
                }
                left++;
            }
        }
        return s.substring(start, end);
    }
}
```