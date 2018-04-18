# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        dummy = ListNode(None)
        dummy.next = head
        curr = head

        while curr.next:
            if curr.val > curr.next.val:
                prev = dummy
                while prev.next.val < curr.next.val:
                    prev = prev.next 
                tmp = curr.next
                curr.next = tmp.next
                tmp.next = prev.next
                prev.next = tmp
            else:
                curr = curr.next
        return dummy.next

        

head = ListNode(1)
node = head
node.next = ListNode(4)
node = node.next
node.next = ListNode(7)
node = node.next
node.next = ListNode(5)
node = node.next
node.next = ListNode(2)

s = Solution()
r = s.insertionSortList(head)
while r:
    print(r.val)    
    r = r.next
   