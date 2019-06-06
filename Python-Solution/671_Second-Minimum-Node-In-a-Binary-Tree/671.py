# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root or not root.left or not root.right:
            return -1

        q = [root]
        minimum = root.val
        vals = set()

        while q:
            node = q.pop(0)
            vals.add(node.val)
            if node.val == minimum:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        if len(vals) == 1:
            return -1
        return sorted(list(vals))[1]