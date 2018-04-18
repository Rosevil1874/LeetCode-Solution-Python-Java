# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        # 将链表平分为前半部分head和后半部分slow
        fast = slow = prev = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None

        # 将后半部分反转反转后为tmp
        curr = slow
        if not curr.next:
            right = slow
        else:
            while curr.next:
                tmp = ListNode(curr.next.val)
                tmp.next = slow
                slow = tmp
                curr.next = curr.next.next
            right = tmp
        
        # 比较两截链表
        left = head
        while left:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True 

head = ListNode(1)
node = head
node.next = ListNode(4)
node = node.next
node.next = ListNode(7)
node = node.next
node.next = ListNode(4)
node = node.next
node.next = ListNode(1)

s = Solution()
r = s.isPalindrome(head)
# while r:
#     print(r.val)    
#     r = r.next
print(r)
   