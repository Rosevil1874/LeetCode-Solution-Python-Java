# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0						# 最大深度
        level = [root] if root else []	# 当前层中包含的树节点
        while level:
        	depth += 1					# 深度加上当前层的1
        	queue = []					# 放置下一层的节点
        	for node in level:			# 遍历这一层所有节点，获取其子节点
        		if node.left:
        			queue.append(node.left)
        		if node.right:
        			queue.append(node.right)
        	level = queue				# 接下来就遍历下一层的子节点啦
        return depth 					# 遍历完之后树的最大深度就求出来啦
        
# 这题就不先构建树来验证了       
# tree = [3,9,20,null,null,15,7]

