# 61 - 旋转链表

## 题目描述
![problem](images/61.png)

>审题：就是把单链表想象成一个循环链表，向右转k个位置。

## 一、双指针
**特殊情况：**
1. 链表长度为0或1，直接返回；
2. k是链表长度的整数倍，直接返回

**思路：**
1. fast指针比slow先走k步；
2. 两指针同时向后遍历直到fast指针指向最后一个结点，此时slow指向倒数第k个结点；
3. fast指向头结点，slow指向None。
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        
        # 求链表长度
        l = 1
        curr = head
        while curr.next:
            curr = curr.next
            l += 1

        k %= l
        if k == 0:
            return head
        
        # 若待旋转次数不是链表长度的整数倍则还需要旋转
        slow = fast = head
        for i in range(k):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        new_head = slow.next
        slow.next = None
        fast.next = head
        return new_head
```


## 二、成环
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        
        # 求链表长度
        l = 1   
        tail = head
        while tail.next:
            tail = tail.next
            l += 1
        tail.next = head    # 将链表成环
        
        # 若待旋转次数不是链表长度的整数倍则还需要旋转
        k %= l
        for i in range(l - k):
            head = head.next
            tail = tail.next
        tail.next = None    # 切断环，成单链表
        return head
```