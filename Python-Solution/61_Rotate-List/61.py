# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 链表长度为0或1，直接返回
        if head is None or head.next is None:
        	return head

        # 计算链表长度
        n = 1
        p = head
        while p.next is not None:
        	p = p.next
        	n += 1

        # k是链表长度的整数倍，直接返回
        if k % n == 0:
        	return head

        k %= n
        p = head
        slow = p
        fast = p
        while k > 0 and fast.next is not None:
        	fast = fast.next
        	k -= 1

        while fast.next is not None:
        	fast = fast.next
        	slow = slow.next
        newHead = slow.next
        fast.next = head
        slow.next = None
        return newHead

head = ListNode(1)
node = head
for i in range(4):
    node.next = ListNode(i+2)
    node = node.next

s = Solution()
r = s.rotateRight(head, 2)
while r:
    print(r.val)
    r = r.next       