# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        l = len(lists)
        if l == 0:
            return None
        while l > 1:
            k = (l + 1) // 2
            for i in range(l // 2):
                lists[i] = self.mergeTwoLists(lists[i], lists[i + k])
            l = k
        return lists[0]

    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        res = head
        while l1 and l2:
            if l1.val < l2.val:
                res.next = l1
                l1 = l1.next
            else:
                res.next = l2
                l2 = l2.next
            res = res.next
        if l1:
            res.next = l1
        elif l2:
            res.next = l2
        return head.next
        

s = Solution()
r = s.mergeKLists(3)
print(r)