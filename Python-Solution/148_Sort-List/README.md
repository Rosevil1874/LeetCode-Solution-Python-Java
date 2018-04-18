---
title: 148 - 链表排序
date: 2018-04-17
tags:
- LeetCode
- Python
- 链表
- 排序
- 双指针
categories: LeetCode
---

## 题目描述
![problem](images/148.png)

<!-- more -->

>审题
题目要求时间复杂度为O(nlogn) 且空间复杂度为常数级。
首先排除掉时间复杂度为O(n^2)的比较排序：冒泡、选择、插入，以及O(n^1.3)的希尔排序；
其次从剩下的快速排序、堆排序、归并排序中排除空间复杂度为O(nlogn)的快速排序和O(n)的归并排序。
So..虽然符合题意的是堆排序，但是要自己实现堆好麻烦。考虑到单链表的操作还是选归并吧。

常用排序的时空复杂度:
![problem](images/sort.jpg)


## 方法一
1. 双指针：找到中间结点，将链表分成两个部分；
2. 递归：对前后每一部分分别归并排序；
3. 合并：将排好序的子链表合并。

```python
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        fast = slow = prev = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        return self.merge( self.sortList(head), self.sortList(slow) )

    def merge(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.merge(l1.next, l2)
            return l1
        else:
            l2.next = self.merge(l1, l2.next)
            return l2
```
个人觉得这个代码写的很厉害（当然是大神写的），虽然能正确解题不过递归深度超限了。。。
![problem](images/error.jpg)

## 方法二
那就把merge改为迭代吧。
哈哈哈过了真开心呦呦✧*｡٩(ˊᗜˋ*)و✧*｡
```python
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        fast = slow = prev = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        return self.merge( self.sortList(head), self.sortList(slow) )

    def merge(self, l1, l2):
        dummy = ListNode(None)
        curr = dummy
        p1 = l1
        p2 = l2
        while p1 and p2:
            if p1.val < p2.val:
                curr.next = p1
                p1 = p1.next
            else:
                curr.next = p2
                p2 = p2.next
            curr = curr.next
        if p1:
            curr.next = p1
        if p2:
            curr.next = p2
        return dummy.next
```