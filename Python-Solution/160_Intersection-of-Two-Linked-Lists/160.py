# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        # 求两链表长度
        p1 = headA
        p2 = headB
        lenA = 0
        lenB = 0
        while p1:
            lenA += 1
            p1 = p1.next
        while p2:
            lenB += 1
            p2 = p2.next

        # 判断链表长短
        diff = 0
        if lenA >= lenB:
            diff = lenA - lenB
            longL = headA
            shortL = headB
        else:
            diff = lenB - lenA
            longL = headB
            shortL = headA

        # 长链表先走diff步
        p1 = longL
        p2 = shortL
        while diff:
            p1 = p1.next
            diff -= 1

        # 两链表同时遍历
        while p2:
            if p1.val == p2.val:
                return p1
            p1 = p1.next
            p2 = p2.next
        return None



# 两个链表相交于结点值为3处
head = ListNode(1)
node = head
node.next = ListNode(2)
node = node.next
node.next = ListNode(3)

head2 = ListNode(11)
node2 = head2
node2.next = ListNode(22)
node2 = node2.next
node2.next = ListNode(33)
node2 = node2.next
node2.next = node.next

node = node.next
node.next = ListNode(4)
node = node.next
node.next = ListNode(5)

s = Solution()
r = s.getIntersectionNode(head, head2)
# while r:
#     print(r.val)
#     r = r.next
print(r.val)    
   