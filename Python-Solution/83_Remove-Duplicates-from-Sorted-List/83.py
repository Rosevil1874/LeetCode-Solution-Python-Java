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

        tail = head   # 最后一个不重复的结点
        p = head.next
        while p is not None:
            if tail.val == p.val:
                p = p.next
                tail.next = tail.next.next
            else:
                p = p.next
                tail = tail.next
        return head

head = ListNode(1)
node = head
# for i in range(4):
#     node.next = ListNode(1)
#     node = node.next
node.next = ListNode(2)
node = node.next
node.next = ListNode(2)

s = Solution()
r = s.deleteDuplicates(head)
while r:
    print(r.val)
    r = r.next       