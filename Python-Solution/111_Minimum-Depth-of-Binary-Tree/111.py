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
        
# 这题就不先构建树来验证了       
# tree = [3,9,20,null,null,15,7]

