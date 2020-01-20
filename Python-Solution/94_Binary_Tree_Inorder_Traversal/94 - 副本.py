# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            curr = stack.pop()
            res.append(curr.val)
            root = curr.right
        return res
		

head = ListNode(1)
node = head
# node.next = ListNode(5)
for i in range(4):
	node.next = ListNode(i+2)
	node = node.next

s = Solution()
r = s.reverseBetween(head, 2, 4)
while r:
	print(r.val)
	r = r.next       