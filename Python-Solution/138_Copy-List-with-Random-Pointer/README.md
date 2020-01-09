# 138 - 复制带随机指针的链表

## 题目描述
![problem](images/138.png)

>审题：
深拷贝：拷贝所有对象，这里就是值链表和每个结点上的随机指针

## 一、哈希
两次遍历链表；
1. 第一次：遍历的同时生成新结点，并建立一个原结点与新结点的哈希表；
2. 第二次：查找哈希表给结点上的随机指针赋值。
3. 使用字典实现哈希表。
```python
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        # 新链表
        prev = RandomListNode(-1)
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
```


## 二、链表拆分
两次遍历链表：
1. 第一次：在原链表的每个结点后拷贝一个新结点；
2. 第二次：依次添加random指针；
3. 删除原结点，将新链表拆分出来。
![copy](images/copy.png)

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        
        # 第一次遍历：拷贝每一个结点到相邻位置
        curr = head
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = curr.next.next
        
        # 第二次遍历：拷贝random指针
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
             
        # 拆分链表
        new_head = head.next
        old, new = head, new_head
        while new.next:
            old.next = new.next
            old = old.next
            new.next = old.next
            new = new.next
        new.next = None
        return new_head
```
