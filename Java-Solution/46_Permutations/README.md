# 46 - 全排列


## 回溯/DFS

```java
class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new LinkedList<>();    // 结果
        LinkedList<Integer> path = new LinkedList<>();         // 路径
        backtrack(res, nums, path);
        return res;
    }

    private void backtrack(List<List<Integer>> res, int[] nums, LinkedList<Integer> path){
        if (path.size() == nums.length) {
            res.add(new LinkedList(path));   // 必须拷贝
            return;
        }

        for (int i = 0; i < nums.length; i++) {
            // 不合法路径
            if (path.contains(nums[i])) {
                continue;
            }
            path.add(nums[i]);
            backtrack(res, nums, path);
            path.removeLast();
        }
    }
}
```