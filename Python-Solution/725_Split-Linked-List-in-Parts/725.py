# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        if not root:
        	return [None]*k

        curr = root
        length = 1
        while curr.next:
        	length += 1
        	curr = curr.next

        parts_len = length // k				# 每个部分的长度，长的部分比起多1
        long_parts_len = parts_len + 1		# 每个部分的长度，长的部分比起多1
        long_num = length % k				# 比较长的部分的个数

        curr = root
        res = []
        for i in range(long_num):
        	part = root
        	n = long_parts_len
        	while n > 1 and root:
        		root = root.next
        		n -= 1
        	tmp = root.next
        	root.next = None
        	root = tmp
        	res.append(part)
        for i in range(long_num, k):
        	part = root
        	n = parts_len
        	while n > 1 and root:
        		root = root.next
        		n -= 1
        	if root:
	        	tmp = root.next
	        	root.next = None
	        else:
	        	tmp = None
        	root = tmp
        	res.append(part)
        return res


head = ListNode(1)
node = head
for i in range(9):
	node.next = ListNode(i+2)
	node = node.next

s = Solution()
r = s.splitListToParts(head, 3)
for i in range(3):  
	node = r[i]
	if node:
		while node:
			print(node.val)
			node = node.next
		print('\n')
	else:
		print(node)
