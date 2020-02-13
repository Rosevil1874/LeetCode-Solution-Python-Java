# 103 - 二叉树的锯齿形层次遍历
## 题目描述
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).


## 题解：

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        direction = 1			# 方向
        curr_level = [root] if root else []
        
        while curr_level:
            next_level = []
            res.append(node.val for node in curr_level[::direction])
            direction *= -1     # 反向
            for node in curr_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            curr_level = next_level
        return res
```
