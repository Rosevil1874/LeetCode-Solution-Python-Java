# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return

        # 划分两个子链表
        fast = slow = prev = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        rightList = slow
        prev.next = None

        # # 将右半部分子链表逆序
        curr = rightList
        while curr.next:
            tmp = ListNode(curr.next.val)
            tmp.next = rightList
            rightList = tmp
            curr.next = curr.next.next
        rightList = tmp

        # 将逆序后的右子链表结点依次插入左子链表
        left = left_prev = head
        right = rightList
        while left:
            left_prev = left
            tmp = ListNode(right.val)
            tmp.next = left.next
            left.next = tmp
            left = left.next.next
            right = right.next
        # 若序列含奇数个结点，把右子链表剩余的那个结点加到末尾
        if right:
            left_prev.next.next = right
        return head

head = ListNode(1)
node = head
for i in range(4):
	node.next = ListNode(i+2)
	node = node.next

s = Solution()
r = s.reorderList(head)
while r:
    print(r.val)    
    r = r.next
   