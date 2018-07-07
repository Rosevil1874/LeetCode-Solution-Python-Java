# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        else:
            # 走到链表末端
            newHead = self.reverseList(head.next)
            # 将前结点设为后结点的后置结点-指针反向
            head.next.next = head
            head.next = None
            
            return newHead
        

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
r = s.reverseList(head)
while r:
    print(r.val)
    r = r.next       