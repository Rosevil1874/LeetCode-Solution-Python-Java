# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def reverseBetween(self, head, m, n):
		"""
		:type head: ListNode
		:type m: int
		:type n: int
		:rtype: ListNode
		"""
		if head is None or head.next is None or m == n:
			return head

		dummy = ListNode(None)
		dummy.next = head
		curr = dummy

		while m-1 :
		    curr = curr.next
		    m -= 1

		prev = curr
		front = None
		end = curr.next
		for i in range( m, n+1 ):
		    curr = prev.next
		    prev.next = curr.next
		    curr.next = front
		    front = curr
		curr = prev.next
		prev.next = front
		end.next = curr
		return dummy.next
		

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