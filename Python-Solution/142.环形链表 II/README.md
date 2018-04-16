---
title: 142 - 环形链表 II
date: 2018-04-14 16:15:08
tags:
- LeetCode
- Python
- 链表
- 双指针
categories: LeetCode
---

## 题目描述
![problem](images/1.png)

<!-- more -->

## 双指针
>cr:[[leetcode]Linked List Cycle II @ Python
](http://www.cnblogs.com/zuoyuan/p/3701877.html)

思路：
1. 使用两个移动速度不同的指针，fast指针的步长为slow指针的两倍；
2. 若两指针相遇则存在环,否则不存在环；
3. 相遇后fast指针不动，slow指针回到起点，两指针同时以相同步长前进，第二次相遇的节点即为环入口。

>示意图：
![principle](images/principle.png)
变量：
1. head到环路起点的距离为K，
2. 环路起点到两指针相遇点的距离为M，
3. 环路周长为L，
4. 两指针相遇时fast走了Lfast，slow走了Lslow。
推导：
1. lslow = K + M; Lfast = K + M + L*n; Lfast = 2*Lsslow
2. Lslow = n * L; K = n * L - M
3. K = (n-1) * L + (l - M)
当slow回到head后走了K到达环路起点，L在环路里从M处开始也走了K，把公式里的M抵消掉，两个指针会在环路起点相遇。


```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next == None:
            return None

        fast = slow = head
        met = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
                
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return fast
        return None
```