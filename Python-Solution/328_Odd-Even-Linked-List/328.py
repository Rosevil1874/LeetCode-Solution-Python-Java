# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """ 
        # 少于三个结点的都不用移动，直接返回
        if not head or not head.next or not head.next.next:
            return head

        # 将odd单独分出来组成一个子链表，然后把剩余的even链表接在其后
        odd = head
        even = evenHead = head.next
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head

head = ListNode(1)
node = head
node.next = ListNode(2 )
node = node.next
node.next = ListNode(3)
node = node.next
node.next = ListNode(4)
node = node.next
node.next = ListNode(5)

s = Solution()
r = s.oddEvenList(head)
while r:
    print(r.val)    
    r = r.next
   