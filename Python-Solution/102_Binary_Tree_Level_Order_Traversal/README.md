# 102 - 层次遍历二叉树
## 题目描述
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).


## 题解：

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        curr_level = [root] if root else []
        
        while curr_level:
            curr_vals = []
            next_level = []
            for node in curr_level:
                curr_vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            res.append(curr_vals)
            curr_level = next_level
        return res
```
