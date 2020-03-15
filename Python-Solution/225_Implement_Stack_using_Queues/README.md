# 225 - [用队列实现栈](https://leetcode.com/problems/implement-stack-using-queues/)

## 题解
每次push之后将队列反转为栈顶处于最左的顺序，即可使用popleft()方便的出栈。push操作O(n)，其他操作Q(1).
```python
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = collections.deque()
        self.capacity = 0       # 栈的容量
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        s = self.stack
        s.append(x)
        self.capacity += 1
        for i in range(self.capacity - 1):
            s.append(s.popleft())
        
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        self.capacity -= 1
        return self.stack.popleft()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.stack[0]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.capacity == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
```