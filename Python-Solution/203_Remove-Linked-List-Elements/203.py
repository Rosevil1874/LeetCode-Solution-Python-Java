# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None

        dummy = ListNode(None)
        dummy.next = head
        prev = dummy
        curr = head

        while curr:
            if curr.val == val:
                prev.next = curr.next
                curr = prev.next
            else:
                prev = prev.next
                curr = curr.next
        return dummy.next

head = ListNode(1)
node = head
node.next = ListNode(2)
node = node.next
node.next = ListNode(4)
node = node.next
node.next = ListNode(3)
node = node.next
node.next = ListNode(2)
node = node.next
node.next = ListNode(5)
node = node.next
node.next = ListNode(2)

s = Solution()
r = s.removeElements(head, 2)
while r:
    print(r.val)
    r = r.next       