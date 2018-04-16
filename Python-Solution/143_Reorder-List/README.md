---
title: 143 - 重排链表
date: 2018-04-15 15:50:34
tags:
- LeetCode
- Python
- 链表
- 双指针
categories: LeetCode
---

## 题目描述
![problem](images/143.png)

<!-- more -->

## 双指针
1. prev指针指向头结点，tail指针指向尾结点,tail_prev指向倒数第二个结点（辅助删除尾结点）；
2. 将tail指针指向的结点移动到prev指针之后；
3. prev指针向后移动两部，tail指针向前移动一步；
4. 知道两指针相遇。

阿欧，指针怎么向前移动啊智障。。。
ding~(此处有个小灯泡)，把后半部分逆序吧，这样就相当于：
1. 把链表从中点分成前后两个子链表；
2. 把后半部分链表逆序；
3. 依次将后半部分链表中的结点插入到前半部分。

```python
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return

        # 划分两个子链表
        fast = slow = prev = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        rightList = slow
        prev.next = None

        # # 将右半部分子链表逆序
        curr = rightList
        while curr.next:
            tmp = ListNode(curr.next.val)
            tmp.next = rightList
            rightList = tmp
            curr.next = curr.next.next
        rightList = tmp

        # 将逆序后的右子链表结点依次插入左子链表
        left = left_prev = head
        right = rightList
        while left:
            left_prev = left
            tmp = ListNode(right.val)
            tmp.next = left.next
            left.next = tmp
            left = left.next.next
            right = right.next
        # 若序列含奇数个结点，把右子链表剩余的那个结点加到末尾
        if right:
            left_prev.next.next = right
        return head
```

## Error
![error](images/error.png)
人家说了不需要返回值嘛，最后检验的还是head为头结点的链表是否已经重排，So...只要保证在原链表重排就行，不要return一个ListNode。
