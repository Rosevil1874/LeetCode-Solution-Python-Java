# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :rtype: int
        """
        for val in self.inorder(root):
        	if k == 1:
        		return val
        	else:
        		k -= 1

    def inorder(self, root):
    	if root:
    		for val in self.inorder(root.left):
    			yield val
    		yield root.val
    		for val in self.inorder(root.right):
    			yield val
        
