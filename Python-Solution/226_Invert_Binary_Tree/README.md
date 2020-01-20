# 226 - 翻转二叉树

## 题目描述
求一棵二叉树的镜像


## 一、递归
real 慢： `Runtime: 32 ms, faster than 22.29% of Python3 online submissions`。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return
        self.swap_nodes(root)
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    
    def swap_nodes(self, node: TreeNode):
        left = node.left
        node.left = node.right
        node.right = left  
```

简化：
```python
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return None
        left = root.left
        right = root.right
        root.right = self.invertTree(left)
        root.left = self.invertTree(right)
        return root
```

再简化：
```python
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        invert = self.invertTree
        if root:
            root.left, root.right = invert(root.right), invert(root.left)
        return root
```


## 二、迭代
```python
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack += node.left, node.right
        return root
```