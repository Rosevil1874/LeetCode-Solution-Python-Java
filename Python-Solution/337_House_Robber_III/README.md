# 337 - 打家劫舍Ⅲ

## 题目描述
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.


### 题解

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(self.helper(root))
        
    def helper(self, root:TreeNode) -> ListNode(int):
        # 返回now和later中较大的值
        # now: 小偷偷当前房子能得到的最大收入
        # later: 小偷不偷当前房子能得到的最大收入
        
        # base case
        if not root:
            return (0, 0)
        
        # left[0],left[1]：小偷偷左子房间和左子房间下一间房间得到的最大收入
        left, right = self.helper(root.left), self.helper(root.right)
        now = root.val + left[1] + right[1]
        later = max(left) + max(right)
        
        return (now, later)
```
