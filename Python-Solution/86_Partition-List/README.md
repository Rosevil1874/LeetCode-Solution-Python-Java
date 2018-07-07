# 86 - 分隔链表

## 题目描述
![problem](images/86.png)

## 双指针
1. 指针1指向小于x的最后一个结点；
2. 指针2依次扫描，若大于x则继续向后，若小于x则将此结点移动到指针1之后，并更新指针1。
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        # 从头开始找到链表前面部分小于x的最后一个结点
        dummy = ListNode(None)
        dummy.next = head 
        tail = dummy    # tail:最后一个小于x的结点
        while tail.next and tail.next.val < x:
            tail = tail.next

        # 若所有结点都小于x，直接返回
        if not tail.next:
            return head

        # 依次将链表后面小于x的结点移动到最后一个小于x的结点后
        curr = tail.next    
        while curr.next: 
            if curr.next.val < x:
                tmp = ListNode(curr.next.val)
                tmp.next = tail.next
                tail.next = tmp
                tail = tail.next
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next
```

## 双链表
1. 分别新建两个空链表；
2. 将小于x的结点尾插法加入链表1， 大于等于x的结点尾插法加入链表2；
3. 将链表2接在链表1尾部，返回链表1；
4. 尾插法是为了保证相对位置不变。

```python
if head is None or head.next is None:
            return head

left = ListNode(None)
right = ListNode(None)
l_tail, r_tail = left, right
while head:
    tmp = head.next
    if head.val < x:
        head.next = None
        l_tail.next = head
        l_tail = l_tail.next
    else:
        head.next = None
        r_tail.next = head
        r_tail = r_tail.next
    head = tmp
l_tail.next = right.next
return left.next
```