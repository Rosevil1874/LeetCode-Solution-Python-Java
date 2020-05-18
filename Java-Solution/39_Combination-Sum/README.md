# 39 - 组合总和


## 回溯法

1. 排序，每次加入一个最小值；
2. 将remain = target-sum(tmp)作为参数进行递归，避免每次计算解中元素的和；
3. 若remain < 0，则表示解中元素的和比target大，从解中pop最后一个元素；
4. 若remain == 0，则找到一个解；

```java
class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<>();
        int len = candidates.length;
        Arrays.sort(candidates);        // 便于剪枝
        backtrack(res, candidates, new ArrayDeque<>(), target, 0);
        return res;
    }

    // path: 当前组合，remain: 剩余数值，start:搜索起点下标
    private void backtrack(List<List<Integer>> res, int[] candidates, Deque<Integer> path, int remain, int start){
        if (remain < 0) {
            return;
        } else if (remain == 0) {
            res.add(new ArrayList<>(path));
            return;
        } else {
            for (int i = start; i < candidates.length; i++){
                if (candidates[i] > remain) {   // 剪枝
                    break;
                }
                path.addLast(candidates[i]);
                // 可以重复使用，所以start是i而不是i+1
                backtrack(res, candidates, path, remain - candidates[i], i);
                path.removeLast();
            }
        }
    }
}
        
```
