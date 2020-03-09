# 199 - [二叉树的右视图](https://leetcode.com/problems/binary-tree-right-side-view/)


## 1. 递归
按'根-右-左'的顺序遍历，每次遍历到新的一层时先访问的是最右节点，将此节点值加入结果中。
```python
# class TreeNode:
#   def __init__(self, x):
#       self.val = x
#       self.left = None
#       self.right = None


class Solution:
    def rightSideView(self, root):
        def helper(node, depth):
            if not node:
                return

            if len(res) == depth:
                res.append(node.val)

            helper(node.right, depth + 1)
            helper(node.left, depth + 1)
            
        res = []
        helper(root, 0)
        return res   
```

## 2. 层次遍历
将每一层最后一个节点加入结果中
```python
# class TreeNode:
#   def __init__(self, x):
#       self.val = x
#       self.left = None
#       self.right = None


class Solution:
    def rightSideView(self, root: TreeNode):
        if not root:
            return []

        curr_level = [root]
        res = []
        while curr_level:
            next_level = []
            res.append(curr_level[-1].val)
            for node in curr_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            curr_level = next_level
        return res
```