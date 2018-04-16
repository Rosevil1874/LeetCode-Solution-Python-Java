---
title: 25 - 每k个一组翻转链表
date: 2018-04-11 17:09:34
tags:
- LeetCode
- Python
categories: LeetCode
---

## 题目描述
![problem](/images/25.png)

<!-- more -->

>审题：
仔细审题说三遍啊，看到这个题目才想起来24题我的第一个蠢蠢的方法不止蠢还不符合题目要求orz
**你不应该改变节点的值，只有节点位置本身可能会改变**

## 方法
1. 首先要知道如何反转链表；
2. 按结点数确定分组；
3. 对确定的分组使用尾插法逆置，然后设置新的起点；
3. 若最后没有k个结点直接跳过。
```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        pre = tail = ListNode(-1)
        q = head
        while q is not None:
            # 向后查找k个结点
            n = k
            p = q
            while p is not None and n > 0:
                p = p.next
                n -= 1

            # 若在查找到k个结点过程中遇到None，说明后面不足k个
            if n > 0:
                tail.next = q
                break

            # 将这k个结点逆置
            end = q
            while q != p:
                t = q.next
                q.next = tail.next
                tail.next = q
                q = t
            tail = end
        return pre.next
```