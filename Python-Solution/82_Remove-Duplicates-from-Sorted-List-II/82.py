# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None or head.next is None:
            return head

        dummy = ListNode(None)
        dummy.next = head

        tail = dummy   # 最后一个不重复的结点
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                    tail.next = tail.next.next
                tail.next = tail.next.next
            else:
                tail = tail.next
            curr = curr.next
        head = dummy.next
        return head

head = ListNode(2)
node = head
for i in range(4):
    node.next = ListNode(1)
    node = node.next
node.next = ListNode(2)
node = node.next
node.next = ListNode(1)

s = Solution()
r = s.deleteDuplicates(head)
while r:
    print(r.val)
    r = r.next       