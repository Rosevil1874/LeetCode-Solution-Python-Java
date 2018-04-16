---
title: 206 - 反转链表
date: 2018-04-14 10:01:12
tags:
- LeetCode
- Python
- 链表
categories: LeetCode
---

## 题目描述
![problem](/images/206.png)

<!-- more -->

>审题：
1. 原地反转一个单链表；
2. 使用迭代和递归两种方法。


## 迭代
头插法：向后遍历，依次将结点插到第一个结点前。
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        curr = head
        while curr.next:
            tmp = ListNode(curr.next.val)
            tmp.next = head
            head = tmp
            curr.next = curr.next.next
        return tmp
```


## 递归
>cr:[全面分析再动手的习惯：链表的反转问题（递归和非递归方式）](http://www.cnblogs.com/kubixuesheng/p/4394509.html)
思路：
1. 递归先走到链表末端；
![step1](/images/step1.png)
2. 更新每个结点的next值，即将指针反向；
![step2](/images/step2.png)
3. 每个指针反向就链表反转了。
![step3](/images/step3.png)

```python
if head is None or head.next is None:
    return head
else:
    # 走到链表末端
    newHead = self.reverseList(head.next)
    # 将前结点设为后结点的后置结点-指针反向
    head.next.next = head
    head.next = None
    
    return newHead
```