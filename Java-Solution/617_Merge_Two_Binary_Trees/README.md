# 617 - 合并二叉树

## 题目描述
合并两棵二叉树，相同位置均有结点的，合并后的结点为两结点值之和；相同位置只有一棵树有结点的，合并后的结点为这个结点值。


```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 and t2:
            new_node = TreeNode(t1.val + t2.val)
            new_node.left = self.mergeTrees(t1.left, t2.left)
            new_node.right = self.mergeTrees(t1.right, t2.right)
            return new_node
        else:
            return t1 or t2
```