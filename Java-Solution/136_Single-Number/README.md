# 136 - 只出现一次的数字


## 题解一
**对于任何数x，都有x^x=0，x^0=x**

```Java
class Solution {
    public int singleNumber(int[] nums) {
        int single = 0;
        for (int  num: nums) {
            single ^= num;
        }
        return single;
    }
}
```
