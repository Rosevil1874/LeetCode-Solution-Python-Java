class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # 将新加入的栈顶元素放在s[-1][0]，最小值放在s[-1][1]，这里的getMin就是自己实现的取最小值的函数。
        # 要判断栈为空的情况，否则getMin返回的是None
        self.s.append((x, x if not self.s else min(self.getMin(), x))) 
        

    def pop(self):
        """
        :rtype: None
        """
        self.s.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.s[-1][0] if self.s else None

    def getMin(self):
        """
        :rtype: int
        """
        return self.s[-1][1] if self.s else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()