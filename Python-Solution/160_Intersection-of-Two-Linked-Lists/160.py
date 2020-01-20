# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        
        lenA, lenB = 0, 0
        pA, pB = headA, headB
        while pA:
            lenA += 1
            pA = pA.next
        while pB:
            lenB += 1
            pB = pB.next
        
        diff = 0
        if lenA <= lenB:
            short = headA
            long = headB
            diff = lenB - lenA
        else:
            short = headB
            long = headA
            diff = lenA - lenB
            
        while diff:
            long = long.next
            diff -= 1
        while short:
            if long.val == short.val:
                return long
            long = long.next
            short = short.next
        return None
        



# 两个链表相交于结点值为3处
head = ListNode(1)
node = head
node.next = ListNode(2)
node = node.next
node.next = ListNode(3)
node = node.next
node.next = ListNode(4)
node = node.next
node.next = ListNode(5)


head2 = ListNode(5)
# node2 = head2
# node2.next = ListNode(22)
# node2 = node2.next
# node2.next = ListNode(33)
# node2 = node2.next
# node2.next = node.next


s = Solution()
r = s.getIntersectionNode(head, head2)
# while r:
#     print(r.val)
#     r = r.next
print(r.val)    
   