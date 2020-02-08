# 21 - 合并两个有序链表

## 题目描述
![problem](images/21.png)

## 老老实实翻开数据结构合并吧
1. 判断链表是否为空，若链表为空则返回空链表；
2. 创建一个新的空链表；
3. 创建一个指针pre指向新链表头；
4. 依次判断两个旧链表头结点val大小，pre指向小的那个，且将这个“小链表”的头指针删去；
5. 其中一个旧链表全部接到新链表后，将另一个链表剩下的部分接到新链表。
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        elif not l1:
            return l2
        elif not l2:
            return l1
        
        new_head = ListNode(0)
        curr = new_head
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
            
        if l1:
            curr.next = l1
        elif l2:
            curr.next = l2
        
        return new_head.next
```


## 递归
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1
        else:
            if l1.val <= l2.val:
                l1.next = self.mergeTwoLists(l1.next, l2)
                return l1
            else:
                l2.next = self.mergeTwoLists(l1, l2.next)
                return l2
```