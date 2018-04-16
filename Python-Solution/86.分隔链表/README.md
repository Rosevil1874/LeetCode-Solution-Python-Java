---
title: 86 - 分隔链表
date: 2018-04-13 16:06:05
tags:
- LeetCode
- Python
- 链表
- 双指针
categories: LeetCode
---

## 题目描述
![problem](images/86.png)

<!-- more -->

>审题：


## 双指针
1. 指针1指向小于x的最后一个结点；
2. 指针2依次扫描，若大于x则继续向后，若小于x则将此结点移动到指针1之后，并更新指针1。
**还未调通**
```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        if head is None or head.next is None:
            return head

        dummy = ListNode(None)
        dummy.next = head 
        tail = curr = dummy    # tail:最后一个小于x的结点
        while curr.next: 
            if curr.next.val < x:
                tmp = ListNode(curr.next.val)
                tmp.next = tail.next
                tail.next = tmp
                tail = tail.next
                curr.next = curr.next.next
            else:
                curr = curr.next
        return tail.next
```

## 双链表
1. 分别新建两个空链表；
2. 将小于x的结点尾插法加入链表1， 大于等于x的结点尾插法加入链表2；
3. 将链表2接在链表1尾部，返回链表1；
4. 尾插法是为了保证相对位置不变。

```python
if head is None or head.next is None:
            return head

left = ListNode(None)
right = ListNode(None)
l_tail, r_tail = left, right
while head:
    tmp = head.next
    if head.val < x:
        head.next = None
        l_tail.next = head
        l_tail = l_tail.next
    else:
        head.next = None
        r_tail.next = head
        r_tail = r_tail.next
    head = tmp
l_tail.next = right.next
return left.next
```