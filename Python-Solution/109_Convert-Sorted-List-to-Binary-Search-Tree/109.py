# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        Rtree = self.findRoot(head)
        root = TreeNode(Rtree.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(Rtree.next)
        return root

    # 找到链表中点作为右子链表的起点返回，并将链表head后半部分切断
    def findRoot(self, head):
        if not head or not head.next:
            return head
        slow = head
        fast = head
        prev = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        return slow

    def printTree(self, root):
        if root is None:
            return
        self.printTree(root.left)
        print(root.val)
        self.printTree(root.right)
        
        

head = ListNode(-10)
node = head
node.next = ListNode(-3)
node = node.next
node.next = ListNode(0)
node = node.next
node.next = ListNode(5)
node = node.next
node.next = ListNode(9)

s = Solution()
r = s.sortedListToBST(head)
if r:     
    s.printTree(r)