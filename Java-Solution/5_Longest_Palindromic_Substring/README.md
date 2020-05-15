# 5 - 最长回文子串

## 中心扩展法
思路：
1. 分别以每个元素为中心，找出偶数长度的最长回文子串和奇数长度的最长回文子串
2. 取奇偶中最长的一个
3. 取所有元素为中心的最长的一个
```java
class Solution {
    public String longestPalindrome(String s) {
        if (s == null || s.length() == 0) return "";
        int start = 0, end = 0;
        // 分别按奇数和偶数字串从中心向两边扩展
        for (int i = 0; i < s.length(); i++) {
            int len1 = expandeAroundCenter(s, i, i);
            int len2 = expandeAroundCenter(s, i, i + 1);
            int len = Math.max(len1, len2);
            if (len > end - start) {
                start = i - (len - 1) / 2;
                end = i + len / 2;
            }
        }
        return s.substring(start, end + 1);
    }

    private int expandeAroundCenter(String s, int left, int right) {
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        return right - left - 1;
    }
}
```
