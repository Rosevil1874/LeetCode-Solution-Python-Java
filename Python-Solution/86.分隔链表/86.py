# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        if head is None or head.next is None:
            return head

        dummy = ListNode(None)
        dummy.next = head 
        tail = curr = dummy    # tail:最后一个小于x的结点
        while curr.next: 
            if curr.next.val < x:
                tmp = ListNode(curr.next.val)
                tmp.next = tail.next
                tail.next = tmp
                tail = tail.next
                curr.next = curr.next.next
            else:
                curr = curr.next
        return tail.next

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
node = node.next
node.next = ListNode(3)
node = node.next
node.next = ListNode(2)
node = node.next
node.next = ListNode(5)

s = Solution()
r = s.partition(head, 3)
while r:
    print(r.val)
    r = r.next       