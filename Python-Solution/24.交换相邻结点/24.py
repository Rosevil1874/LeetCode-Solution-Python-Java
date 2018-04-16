# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        tmp = head.next
        head.next = swapPairs(tmp.next)
        tmp.next = head
        return tmp

            
head = ListNode(1)
node = head
for i in range(4):
    node.next = ListNode(i+2)
    node = node.next

s = Solution()
r = s.swapPairs(head)
while r:
    print(r.val)
    r = r.next