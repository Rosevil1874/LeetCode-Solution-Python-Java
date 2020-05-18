# 17 - 电话号码的字母组合

## 回溯全排列

```java
class Solution {
    String[] letter_map = {"","*","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
    List<String> res = new ArrayList<String>();

    public void backtrack(String combination, String digits, int index) {
        // this turn of dfs is done
        if (digits.length() == index) {
            res.add(combination);
            return;
        }
        // if there are still digits to check
        else {
            String letters = letter_map[digits.charAt(index) - '0'];
            for (int i = 0; i < letters.length(); i++){
                backtrack(combination + letters.charAt(i), digits, index + 1);
            }
        }
    }

    public List<String> letterCombinations(String digits) {
        if (digits.length() != 0){
            backtrack("", digits, 0);
        }
        return res;
    }
}
```
