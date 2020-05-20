# 49 - 变位词分组

## 题目描述
Given an array of strings, group anagrams together.

**Example:**
**Input:** ["eat", "tea", "tan", "ate", "nat", "bat"],
**Output:**
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

**Note:**
All inputs will be in lowercase.
The order of your output does not matter.


```java
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> hash = new HashMap<>();

        for (int i = 0; i < strs.length; i++) {
            // 转换成数组排序再转换回字符串
            char[] s_arr = strs[i].toCharArray();
            Arrays.sort(s_arr);
            String key = String.valueOf(s_arr);

            if (hash.containsKey(key)) {
                hash.get(key).add(strs[i]);
            } else {
                List<String> temp = new ArrayList<String>();
                temp.add(strs[i]);
                hash.put(key, temp);
            }
        }
        return new ArrayList<List<String>>(hash.values());
    }
}
```