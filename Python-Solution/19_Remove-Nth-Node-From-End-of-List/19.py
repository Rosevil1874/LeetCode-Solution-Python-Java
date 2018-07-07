# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 空链表：返回空链表
        if head is None:
        	return None
        # 不用删：返回原链表
        if n == 0:
        	return head

        # 快慢指针
        fast = head
        slow = head

        # 快指针移动N个结点
        for i in range(n):
        	fast = fast.next

        # 删除第一个结点
        if fast is None:
        	return head.next

        # 快慢指针同时后移
        while fast.next != None:
        	fast = fast.next
        	slow = slow.next
        # 删结点
        slow.next = slow.next.next
      	return head
