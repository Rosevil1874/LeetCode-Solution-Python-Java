# 15 - 三数之和

## 双指针
1. 将数组排序；
2. 第一层循环遍历元素到倒数第三个【第一个数】；
3. 第二层循环使用双指针在剩余位置由两端向中间靠拢检查【后两个数】；
4. 符合条件且不重复的加入结果数组。

> Runtime: 908 ms, faster than 63.40% of Python3 online submissions

```java
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList();
        Arrays.sort(nums);      // 排序,便于去重
        int len = nums.length;

        for (int i = 0; i < len - 2; i++) {
            // 去重
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            int l = i + 1;
            int r = len - 1;
            while (l < r) {
                int sum = nums[l] + nums[i] + nums[r];
                if (sum == 0) {
                    res.add(Arrays.asList(nums[l], nums[i], nums[r]));
                    l++;
                    r--;
                    // 去重
                    while(l < r && nums[l] == nums[l - 1]) l++;
                    while(l < r && nums[r] == nums[r + 1]) r--;
                } 
                else if (sum < 0) l++;
                else if (sum > 0) r--;
            }
            
        }
        return res;
    }
}
```
