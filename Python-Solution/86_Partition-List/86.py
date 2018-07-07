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

        # 从头开始找到链表前面部分小于x的最后一个结点
        dummy = ListNode(None)
        dummy.next = head 
        tail = dummy    # tail:最后一个小于x的结点
        while tail.next and tail.next.val < x:
            tail = tail.next

        # 若所有结点都小于x，直接返回
        if not tail.next:
            return head

        # 依次将链表后面小于x的结点移动到最后一个小于x的结点后
        curr = tail.next    
        while curr.next: 
            if curr.next.val < x:
                tmp = ListNode(curr.next.val)
                tmp.next = tail.next
                tail.next = tmp
                tail = tail.next
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next

head = ListNode(1)
node = head
node.next = ListNode(1)
# node = node.next
# node.next = ListNode(3)
# node = node.next
# node.next = ListNode(2)
# node = node.next
# node.next = ListNode(5)
# node = node.next
# node.next = ListNode(2)


s = Solution()
r = s.partition(head, 2)
while r:
    print(r.val)
    r = r.next       