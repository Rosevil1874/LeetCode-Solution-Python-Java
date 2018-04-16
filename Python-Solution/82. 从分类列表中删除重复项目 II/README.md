---
title: 82. 从分类列表中删除重复项目 II
date: 2018-04-13 11:12:06
tags:
- LeetCode
- Python
- 链表
- 双指针
categories: LeetCode
---

## 题目描述
![problem](images/82.png)

<!-- more -->

>审题：
注意注意，此题与83题的区别在于：不是说有三个1的话只保留一个1，而是只要1这个数字有重复，就一个不留。

## 双指针
1. 指针1指向不重复的最后一个结点；
2. 指针2依次扫描，若不重复则更新指针1，否则移除。
3. 与83题区别：使用dummy头结点便于删除所有重复值。
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        dummy = ListNode(None)
        dummy.next = head

        tail = dummy   # 最后一个不重复的结点
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                    tail.next = tail.next.next
                tail.next = tail.next.next
            else:
                tail = tail.next
            curr = curr.next
        head = dummy.next
        return head
```