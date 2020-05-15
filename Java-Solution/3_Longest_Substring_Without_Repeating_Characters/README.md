# 3 - 无重复字符的最长子串

## 滑动窗口

```java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        // 记录当前无重复子串中已经出现过的字符
        Set<Character> showed = new HashSet<Character>();
        int n = s.length();
        int start = 0;  //最长无重复子序列的开始坐标
        int maxLen = 0;
        int currLen = 0;
        int left = 0;   //滑动窗口的左边
        for (int i = 0; i < n; i++) {
            currLen += 1;
            while (showed.contains(s.charAt(i))) {
                showed.remove(s.charAt(left));
                left += 1;
                currLen -= 1;
            }
            maxLen = Math.max(maxLen, currLen);
            showed.add(s.charAt(i));
        }
        return maxLen;
    }
}
```