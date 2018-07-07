# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1 = self.reverseList( l1 )
        l2 = self.reverseList( l2 )

        head = ListNode(None)
        curr = head
        carry = 0       # 进位
        while l1 or l2 or carry != 0:
            num = ( l1.val if l1 else 0 ) + ( l2.val if l2 else 0 ) + carry
            carry = num // 10
            curr.next = ListNode(num % 10)
            curr = curr.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        return self.reverseList(head.next)
        
    # 反转链表
    def reverseList(self, head):
        if not head or not head.next:
            return head

        curr = head
        while curr.next:
            tmp = ListNode(curr.next.val)
            tmp.next = head
            head = tmp
            curr.next = curr.next.next
        return tmp


head = ListNode(7)
node = head
node.next = ListNode(2 )
node = node.next
node.next = ListNode(4)
node = node.next
node.next = ListNode(3)

head2 = ListNode(5)
node = head2
node.next = ListNode(6)
node = node.next
node.next = ListNode(4)

s = Solution()
r = s.addTwoNumbers(head, head2)
while r:
    print(r.val)    
    r = r.next