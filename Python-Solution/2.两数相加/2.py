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
        head = ListNode(0)
        curr = head
        carry = 0		# 进位
        while l1 is not None or l2 is not None or carry != 0:
        	num = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
        	carry = num // 10
        	curr.next = ListNode( num % 10 )
        	curr = curr.next
        	l1 = l1.next if l1 else l1
        	l2 = l2.next if l2 else l2
        return head.next