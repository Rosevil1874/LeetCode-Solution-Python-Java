class Node:
	def __init__(self, s, e):
		self.s = s
		self.e = e
		self.left = None
		self.right = None

class MyCalendar:

    def __init__(self):
        self.root = None

    def book_helper(self, start, end, node):
    	if start >= node.e:
    		if node.right:
    			return self.book_helper(start, end, node.right)
    		else:
    			node.right = Node(start, end)
    			return True

    	elif end <= node.s:
    		if node.left:
    			return self.book_helper(start, end, node.left)
    		else:
    			node.left = Node(start, end)
    			return True

    	else:
    		return False

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if self.root:
        	return self.book_helper(start, end, self.root)
        else:
        	self.root = Node(start, end)
        	return True


# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()
book_1 = obj.book(10, 20)
book_2 = obj.book(15, 25)
book_3 = obj.book(20, 30)
print(book_1)
print(book_2)
print(book_3)
    