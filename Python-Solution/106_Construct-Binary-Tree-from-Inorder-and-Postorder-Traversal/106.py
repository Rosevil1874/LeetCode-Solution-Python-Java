# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder ):
        """
        :type postorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None

        root = TreeNode(postorder.pop())
        inIdx = inorder.index(root.val)

        root.right = self.buildTree(inorder[inIdx + 1:], postorder)
        root.left = self.buildTree(inorder[:inIdx], postorder)

        return root
        
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
s = Solution()
r = s.buildTree( inorder, postorder )
print(r.val)     