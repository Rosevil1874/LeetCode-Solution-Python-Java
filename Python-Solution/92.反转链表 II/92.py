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
        prev = dummy
        diff = n - m

        while m-1 :
            prev = prev.next
            m -= 1

        start = prev.next
        then = start.next
        while diff:
        	start.next = then.next
        	then.next = prev.next
        	prev.next = then
        	then = start.next
        	diff -= 1
        return head
        

head = ListNode(1)
node = head
for i in range(2):
	node.next = ListNode(i+2)
	node = node.next

s = Solution()
r = s.reverseBetween(head, 1, 1)
while r:
    print(r.val)
    r = r.next       