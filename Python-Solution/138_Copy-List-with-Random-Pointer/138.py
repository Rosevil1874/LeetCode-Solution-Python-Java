# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """

        # 新链表
        prev = RandomListNode(None)
        tail = prev
        d = {}

        # 第一次遍历：建立新链表
        oldNode = head
        while oldNode:
            newNode = RandomListNode(oldNode.label)
            d[oldNode] = newNode
            tail.next = newNode
            tail = tail.next
            oldNode = oldNode.next

        # 第二次遍历：赋值random指针
        tail = prev.next
        oldNode = head
        while oldNode:
            if oldNode.random:
                tail.random = d[oldNode.random]
            oldNode = oldNode.next
            tail = tail.next

        return prev.next

head = RandomListNode(-10)
node = head
node.next = RandomListNode(-3)
node = node.next
node.next = RandomListNode(0)
node = node.next
node.next = RandomListNode(5)
node = node.next
node.next = RandomListNode(9)

s = Solution()
r = s.copyRandomList(head)
while r:
    print(r.label)
    r = r.next  