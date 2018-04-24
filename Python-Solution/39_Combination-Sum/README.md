# 39 - 组合总和

## 题目描述
![problem](images/39.png)

>审题：  
1. 相同元素可重复使用；
2. 解集不包含重复解；
3. 这是n-sum，不是之前的two-sum、three-sum、four-sum，不能用循环。

## 回溯法

1. 排序，每次加入一个最小值；
2. 将remain = target-sum(tmp)作为参数进行递归，避免每次计算解中元素的和；
3. 若remain < 0，则表示解中元素的和比target大，从解中pop最后一个元素；
4. 若remain == 0，则找到一个解；

```python
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.backtrack(res, [], candidates, target, 0)
        return res

    def backtrack(self, res, tmp, candidates, remain, start):
    	if remain < 0:
    		return
    	elif remain == 0:
    		res.append(tmp)
    	else:
    		for i in range(start, len(candidates)):
    			if candidates[i] > remain:		# 剪枝
    				break
    			# tmp.append(candidates[i])		# tmp按引用传递，直接这样append会导致最后res中的解全部是最后一个tmp的值
    			self.backtrack(res, tmp + [candidates[i]], candidates, remain - candidates[i], i) #可以重复使用同一元素，所以start是i而不是i+1

```
