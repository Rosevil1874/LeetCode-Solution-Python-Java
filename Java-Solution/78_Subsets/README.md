# 78 - 子集

## 迭代
```java
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList();
        res.add(new ArrayList<Integer>());

        for (int num: nums) {
            List<List<Integer>> subsets = new ArrayList();
            for (List<Integer> curr: res) {
                subsets.add(new ArrayList<Integer>(curr){{add(num);}});
            }
            for (List<Integer> curr: subsets) {
                res.add(curr);
            }
        }
        return res;
    }
}
```

## 回溯
```java
class Solution {
    List<List<Integer>> res = new ArrayList();
    int n, k;

    public void backtrack(int first, ArrayList<Integer> curr, int[] nums) {
        if (curr.size() == k) {
            res.add(new ArrayList(curr));
        }

        for (int i = first; i < n; i++) {
            curr.add(nums[i]);
            backtrack(i + 1, curr, nums);
            curr.remove(curr.size() - 1);
        }
    }

    public List<List<Integer>> subsets(int[] nums) {
        n = nums.length;
        // k代表每种可能的子集长度
        for (k = 0; k <= n; k++) {
            backtrack(0, new ArrayList<Integer>(), nums);
        }
        return res;
    }
}
```

## 位运算
>'To give all the possible subsets, we just need to exhaust all the possible combinations of the numbers. And each number has only two possibilities: either in or not in a subset. And this can be represented using a bit.'

```java
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList();
        int n = nums.length;
        
        for (int i = 0; i < (1 << n); i++) {
            List<Integer> subset = new ArrayList();
            for (int j = 0; j < n; j++) {
                if (((i >> j) & 1) == 1) subset.add(nums[j]);
            }
            res.add(subset);
        }
        return res;
    }
}
```