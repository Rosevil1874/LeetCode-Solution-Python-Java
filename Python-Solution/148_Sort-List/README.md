# 148 - 链表排序

## 题目描述
![problem](images/148.png)

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

> 上一次刷题的时候这个代码递归深度超限了没有通过，这次竟然通过了，不过挺慢的。  
Runtime: 264 ms, faster than 20.73% of Python3 online submissions

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        # 将链表平分成两段
        prev = slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        return self.merge_lists(self.sortList(head), self.sortList(slow))
        
        
    def merge_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val <= l2.val:
            l1.next = self.merge_lists(l1.next, l2)
            return l1
        else:
            l2.next = self.merge_lists(l1, l2.next)
            return l2
                
```


## 方法二
那就把merge改为迭代吧。
哈哈哈过了真开心呦呦✧*｡٩(ˊᗜˋ*)و✧*｡

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        # 将链表平分成两段
        prev = slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        return self.merge_lists(self.sortList(head), self.sortList(slow))
        
        
    def merge_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(None)
        curr = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        if l1:
            curr.next = l1
        else:
            curr.next = l2
        return dummy.next
                
```