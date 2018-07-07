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
        if head is None or head.next == None:
            return None

        fast = slow = head
        met = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
                
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return fast
        return None

head = ListNode(1)
node = head
for i in range(9):
	node.next = ListNode(i+2)
	node = node.next
node.next = head

s = Solution()
r = s.hasCycle(head)
print(r.val)       