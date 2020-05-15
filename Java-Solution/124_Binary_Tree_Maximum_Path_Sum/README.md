# 124 - 二叉树中的最大路径和

## 题目描述
![problem](images/124.png)  
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.


## 递归
思路： 最长路径 = 最长左子路径 + 最长右子路径

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_sum = [root.val]   # 数组才能作为参数传到函数中并修改，否则传递的是一个拷贝

        self.find_max(root, max_sum)
        return max_sum[0]
        
        
    def find_max(self, node: TreeNode, max_sum: List[int]) -> int:
        if not node:
            return 0
        
        # 计算左右子树的最长路径
        # 左右子树最长路径分别和0比较，大于0就将此分支放在此路径上，否则剪枝
        left_max = max(self.find_max(node.left, max_sum), 0)
        right_max = max(self.find_max(node.right, max_sum), 0)
        
        # 计算以此节点作为根节点的子树的最长路径
        max_sum[0] = max(max_sum[0], node.val + left_max + right_max)
        
        # 返回左右子路径中较长的一个，否则不构成路径
        return node.val + max(left_max, right_max)
```