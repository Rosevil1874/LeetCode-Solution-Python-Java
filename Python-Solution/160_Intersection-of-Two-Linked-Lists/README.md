# 160 - 相交链表

## 题目描述
![problem](images/160.png)

## 方法一
1. 遍历两链表得到链表长度；
2. 特殊情况：由于求长度时要走到链表尾，这时可以比较两结点。若不相同可直接返回None；
3. 指针1在长链表中先前进链表长度差（lenA-lenB)步，这时两链表剩余长度相同；
4. 两指针同时前进直到找出相同结点并返回，或走完链表仍不同就返回None。

> 此代码无法通过测试用例：  
`
[4,1,8,4,5]
[5,0,1,8,4,5]
`
此代码找出的交点为结点'1'，官方解答为'8'，不太明白为什么这个交点是8呢。。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        
        lenA, lenB = 0, 0
        pA, pB = headA, headB
        while pA:
            lenA += 1
            pA = pA.next
        while pB:
            lenB += 1
            pB = pB.next
        
        diff = 0
        if lenA <= lenB:
            short = headA
            long = headB
            diff = lenB - lenA
        else:
            short = headB
            long = headA
            diff = lenA - lenB
            
        while diff:
            long = long.next
            diff -= 1
        while short:
            if long.val == short.val:
                return long
            long = long.next
            short = short.next
        return None
        
```


## 方法二
1. 将两链表相连成两个新链表：A+B和B+A；
2. 两个新链表的长度相同且有与两原始链表相同的交点，遍历两链表，若找到交点则返回，找不到则会同时遍历到链表尾部的None并返回。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        
        A, B = headA, headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A
            
```