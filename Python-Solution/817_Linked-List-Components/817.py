# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def numComponents(self, head, G):
		"""
		:type head: ListNode
		:type G: List[int]
		:rtype: int
		"""
		if not head:
			return 0

		G = set(G)
		dummy = ListNode(None)
		dummy.next = head
		prev = dummy
		curr = head
		num = 0
		while curr:
			num += prev.val not in G and curr.val in G
			prev = prev.next
			curr = curr.next
		return num


head = ListNode(0)
node = head
for i in range(3):
	node.next = ListNode(i+1)
	node = node.next
G = [0,3,1,4]

s = Solution()
r = s.numComponents(head, G)
print(r)    
