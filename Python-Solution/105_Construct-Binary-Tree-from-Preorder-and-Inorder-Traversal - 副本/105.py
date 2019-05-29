# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder.pop(0))
        inIdx = inorder.index(root.val)

        root.left = self.buildTree(preorder inorder[:inIdx])
        root.right = self.buildTree(preorder, inorder[inIdx + 1 :])

        return root
        
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
s = Solution()
r = s.buildTree(preorder, inorder)
print(r.val)     