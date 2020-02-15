# 108 - 将有序数组转换为二叉搜索树
## 题目描述
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.


## 题解一
先找到平衡BST的root，再递归调用函数构造左右子树。  
**时间复杂度O(nlogn):** slice 时间复杂度为O(n)，递归logn层。
**空间复杂度O(n):** slice传参。
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        
        # 有序数组地中间元素为平衡BST的根节点
        # 其左右子序列分别构成左右子树
        mid = (len(nums)) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        
        return root
```

## 题解二
不使用slice传参，而是传递子序列弃之索引。
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def convert(left, right):
            if left > right:
                return None
        
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = convert(left, mid - 1)
            root.right = convert(mid + 1, right)
            return root
        
        return convert(0, len(nums) - 1)
```