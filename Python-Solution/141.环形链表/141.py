# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        if head.next == head:
            return True

        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
        

head = ListNode(1)
node = head
for i in range(2):
	node.next = ListNode(i+2)
	node = node.next
node.next = head

s = Solution()
r = s.hasCycle(head)
print(r)       