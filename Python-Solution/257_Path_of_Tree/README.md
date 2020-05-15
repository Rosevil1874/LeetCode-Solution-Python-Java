# 257 - 二叉树的所有路径


## 回溯
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.res = []
        if not root:
            return self.res

        
        def find_path(root, path):
            path.append(root.val)
            if not root.left and not root.right:
                self.res.append(path[:])
                return
            if root.left:
                find_path(root.left, path)
                path.pop()
            if root.right:
                find_path(root.right, path)
                path.pop()
            
        find_path(root, [])
        self.res = ['->'.join(list(map(str, item))) for item in self.res]
        return self.res
        
             
```
