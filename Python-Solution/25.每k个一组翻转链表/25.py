# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        pre = tail = ListNode(-1)
        q = head
        while q is not None:
            # 向后查找k个结点
            n = k
            p = q
            while p is not None and n > 0:
                p = p.next
                n -= 1

            # 若在查找到k个结点过程中遇到None，说明后面不足k个
            if n > 0:
                tail.next = q
                break

            # 将这k个结点逆置
            end = q
            while q != p:
                t = q.next
                q.next = tail.next
                tail.next = q
                q = t
            tail = end
        return pre.next
            
head = ListNode(1)
node = head
for i in range(4):
    node.next = ListNode(i+2)
    node = node.next

s = Solution()
r = s.reverseKGroup(head, 3)
while r:
    print(r.val)
    r = r.next