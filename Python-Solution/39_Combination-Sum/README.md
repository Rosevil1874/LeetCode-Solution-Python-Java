# 39 - 组合总和

## 题目描述
![problem](images/39.png)

>审题：  
1. 相同元素可重复使用；
2. 解集不包含重复解；
3. 这是n-sum，不是之前的two-sum、three-sum、four-sum，不能用循环。
4. 关联题目[40.组合总数II](https://github.com/Rosevil1874/LeetCode/tree/master/Python-Solution/40_Combination-Sum-II)，[216.组合总数III](https://github.com/Rosevil1874/LeetCode/tree/master/Python-Solution/216_Combination-Sum-III)

## 回溯法

1. 排序，每次加入一个最小值；
2. 将remain = target-sum(tmp)作为参数进行递归，避免每次计算解中元素的和；
3. 若remain < 0，则表示解中元素的和比target大，从解中pop最后一个元素；
4. 若remain == 0，则找到一个解；

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.backtrack(candidates, res, [], target, 0)
        return res
    
    
    def backtrack(candidates: List[int], res: List[int], tmp: List[int], remain: int, start:int):
        if remain < 0:
            return
        elif remain == 0:
            res.append(tmp)
        else:
            for i in range(start, len(candidates)):
                if candidates[i] > remain:  # 剪枝
                    break
                # tmp按引用传递，直接append会导致最后res中的解全部是最后一个tmp的值
                # 可以重复使用同一元素，所以start是i而不是i+1
                self.backtrack(candidates, res, tmp + [candidates[i]], remain - candidates[i], i)
        
```
