---
title: 92 - 反转链表 II
date: 2018-04-14 10:02:52
tags:
- LeetCode
- Python
- 链表
- 双指针
categories: LeetCode
---

## 题目描述
![problem](images/92.png)

<!-- more -->

>审题：
类似题目：[206.反转链表]()

## 迭代
思路：
1. prev：开始反转的前一个结点
2. start：开始反转的第一个结点
3. then：下一个要插入到prev后面的结点
4. 使用头插法将反转段的结点一个个移动到prev后就行了；

**这个两个代码本地是对的，但是提交上去都不对**
```python
class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head is None or head.next is None or m == n:
            return head

        dummy = ListNode(None)
        dummy.next = head
        prev = dummy
        end = start = head
        diff = n - m
        while diff:
        	end = end.next
        	diff -= 1
        while m-1 :
        	prev = prev.next
        	start = start.next
        	end = end.next
        	m -= 1
        curr = start
        while curr.next != end.next:
            tmp = ListNode(curr.next.val)
            tmp.next = start
            prev.next = tmp
            start = tmp
            curr.next = curr.next.next
        return head
```

```python
if head is None or head.next is None or m == n:
    return head

dummy = ListNode(None)
dummy.next = head
prev = dummy
diff = n - m
while m-1 :
    prev = prev.next
    m -= 1
start = prev.next
then = start.next
while diff:
	start.next = then.next
	then.next = prev.next
	prev.next = then
	then = start.next
	diff -= 1
return head
```