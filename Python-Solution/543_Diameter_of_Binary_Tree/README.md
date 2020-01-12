# 543 - 二叉树的直径

## 题目描述
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.


## 题解：
**思路：** 题目中说二叉树的直径是任意两个结点路径中最长的那一条，最长路径必然是两个叶结点经过根结点的路径，因此：  
对每一个结点： **直径 = 根结点左子树的高度 + 右子树的高度**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0
        self.depth(root)
        return self.diameter
        
    def depth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left, right = self.depth(root.left), self.depth(root.right)
        self.diameter = max(self.diameter, left + right)
        return max(left, right) + 1
```
