# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        res = [float('inf')]
        res = self.dfs(root, root, res)
        return -1 if res[0] == float('inf') else res[0]
        
    def dfs(self, root: TreeNode, curr: TreeNode, res: List[int]) -> List[int]:
        if not curr:
            return
        if root.val < curr.val < res[0]:
            res[0] = curr.val
        self.dfs(root, curr.left, res)
        self.dfs(root, curr.right, res)
        return res