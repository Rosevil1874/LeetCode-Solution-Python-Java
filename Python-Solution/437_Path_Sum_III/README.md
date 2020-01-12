# 437 - 路径综合Ⅲ

## 题目描述
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.


### 一、暴力递归
1. **方法**：遍历所有结点，找到从当前节点开始的和为sum路径；
2. **时间复杂度**：最差情况O(n^2)，当树高度不平衡只有一条分支路径时；最佳情况O(nlogn)，当二叉树平衡时；
3. **空间复杂度**：O(1)。

> Runtime: 956 ms, faster than 16.64% of Python3 online submissions

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        else:
            return self.helper(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        
        
    def helper(self, root: TreeNode, target: int) -> int:
        if not root:
            return 0
        else:
            return int(root.val == target) + self.helper(root.left, target - root.val) + self.helper(root.right, target - root.val)
```


### 二、回溯
1. **方法**：
	- cache{0：1}：从根结点到某结点的和为0的路径有一条；
	- curr_sum：从根结点到当前结点路径的和；
	- old_sum：从根结点到当前路径前面的某个结点的路径和，从curr_sum中去掉old_sum能得到目标；
2. **时间复杂度**：只会遍历一遍二叉树，复杂度为O(n)；
3. **空间复杂度**：cache存放root到每个结点的路径和，复杂度为O(n)。

> Runtime: 44 ms, faster than 93.76% of Python3 online submissions

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.cnt = 0
        cache = {0:1}  
        self.helper(root, sum, 0, cache)
        return self.cnt
        
        
    def helper(self, root: TreeNode, target: int, curr_sum: int, cache: dict) -> int:
        if not root:
            return
        
        curr_sum += root.val
        old_sum = curr_sum - target
        
        self.cnt += cache.get(old_sum, 0)   # 从根结点到多少个此路径前面的结点的和为old_sum，这些结点到当前结点就能组成多少个和为target的路径
        cache[curr_sum] = cache.get(curr_sum, 0) + 1      # 将当前路径和放入cache
        
        self.helper(root.left, target, curr_sum, cache)
        self.helper(root.right, target, curr_sum, cache)
        
        # 回溯
        cache[curr_sum] -= 1
```