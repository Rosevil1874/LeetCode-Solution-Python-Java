# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root, float('-inf'), float('inf'))
        
        
    def helper(self, root: TreeNode, min_val: float, max_val: float) -> bool:
        print(type(root.val),type(min_val))
        if not root:
            return True
        elif root.val <= min_val or root.val >= max_val:
            return False
        return self.helper(root.left, min_val, root.val) and self.helper(root.right, root.val, max_val)
		

root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
s = Solution()
r = s.isValidBST(root)
while r:
	print(r.val)
	r = r.next       