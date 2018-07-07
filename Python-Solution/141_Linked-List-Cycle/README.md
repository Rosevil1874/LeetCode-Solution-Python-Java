# 141 - 环形链表

## 题目描述
![problem](images/141.png)

>关联题目： [142. 环形链表II](https://github.com/Rosevil1874/LeetCode/tree/master/Python-Solution/142_Linked-List-Cycle-II)    


## 双指针
思路：使用两个移动速度不同的指针，若相遇则存在环。

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        if head.next == head:
            return True

        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
```