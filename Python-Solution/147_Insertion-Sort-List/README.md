# 147 - 链表插入排序

## 题目描述
![problem](images/147.png)

## 方法
1. 插入排序
2. 注意链表向后遍历比较方便，所以查找一个元素在有序列表中的正确位置时应该从链表头开始查找。

```python
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        dummy = ListNode(None)
        dummy.next = head
        curr = head

        while curr.next:
            if curr.val > curr.next.val:
                prev = dummy
                while prev.next.val < curr.next.val:
                    prev = prev.next 
                tmp = curr.next
                curr.next = tmp.next
                tmp.next = prev.next
                prev.next = tmp
            else:
                curr = curr.next
        return dummy.next
```