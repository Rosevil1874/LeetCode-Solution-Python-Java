# 94 - 二叉树的中序遍历

## 题目描述
Given a binary tree, return the inorder traversal of its nodes' values.  
Follow up: Recursive solution is trivial, could you do it iteratively?


## 一、递归
中序遍历：左-根-右。  
虽然题目说递归没啥意思还是写写吧。

> Runtime: 28 ms, faster than 63.29% of Python3 online submissions.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.helper(root, res)
        return res
        
    def helper(self, root: TreeNode, res: List[int]) -> List[int]:
        if root:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)
        
```


## 二、迭代
使用栈实现：
1. 先从根结点开始一直向左遍历，到达最左叶子结点，同时将这些结点依次压栈；
2. 从栈中依次pop左子结点，将其值放入结果数组中，同时将当前结点的右子结点作为根重复操作1；
3. 重复上述两步直到栈空。

运行时间和上面一样。
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            curr = stack.pop()
            res.append(curr.val)
            root = curr.right
        return res
            
                
            
        
```
