# 111 - 二叉树的最小深度
## 题目描述
![problem](images/111.png)

>关联题目： [104. 二叉树的最大深度](https://github.com/Rosevil1874/LeetCode/tree/master/Python-Solution/104_Maximum-Depth-of-Binary-Tree)



## 题解
**思路：** 
1. 递归求解：二叉树的最大深度 = min(左子树的最小深度, 右子树的最小深度) + 1；
2. 后面加上的这个1是根节点这一层；
3. 若min子树深度为0，则取另外一个子树的深度。
```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        d = map(self.minDepth, (root.left, root.right))
        return (min(d) or max(d)) + 1
```
