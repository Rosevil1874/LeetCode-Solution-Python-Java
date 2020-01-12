# 114 - 二叉树展开为链表 

## 题目描述
Given a binary tree, flatten it to a linked list in-place.  
根据给的例子，是按先序遍历的顺序展开二叉树，去掉所有左子结点。


### 题解
> ref: [reversed preorder traverse](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/36977/)。从最右叶子节点开始依次将前一个结点的右指针指向自己，前一个结点的左指针指向空。可以看看评论中的图解，便于理解。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.prev = None
        
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return 
        
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.prev
        root.left = None
        
        self.prev = root
        
```
