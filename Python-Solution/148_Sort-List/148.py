# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        fast = slow = prev = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        return self.merge( self.sortList(head), self.sortList(slow) )

    def merge(self, l1, l2):
        dummy = ListNode(None)
        curr = dummy
        p1 = l1
        p2 = l2
        while p1 and p2:
            if p1.val < p2.val:
                curr.next = p1
                p1 = p1.next
            else:
                curr.next = p2
                p2 = p2.next
            curr = curr.next
        if p1:
            curr.next = p1
        if p2:
            curr.next = p2
        return dummy.next

head = ListNode(1)
node = head
node.next = ListNode(4)
node = node.next
node.next = ListNode(7)
node = node.next
node.next = ListNode(5)
node = node.next
node.next = ListNode(2)

s = Solution()
r = s.sortList(head)
while r:
    print(r.val)    
    r = r.next
   