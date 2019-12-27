# 141 - 环形链表

## 题目描述
![problem](images/141.png)

>关联题目： [142. 环形链表II](https://github.com/Rosevil1874/LeetCode/tree/master/Python-Solution/142_Linked-List-Cycle-II)    


## 双指针
思路：使用两个移动速度不同的指针，若相遇则存在环。

>Runtime: 44 ms, faster than 92.40% of Python3 online submissions.  
Memory Usage: 16 MB, less than 100.00% of Python3 online submissions

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return None
        if not head.next:
            return None
        
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
```