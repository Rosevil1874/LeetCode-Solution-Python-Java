# 142 - 环形链表 II

## 题目描述
![problem](images/142.png)

>关联题目： [141. 环形链表](https://github.com/Rosevil1874/LeetCode/tree/master/Python-Solution/141_Linked-List-Cycle)    
>关联题目： [287. 寻找重复数](https://github.com/Rosevil1874/LeetCode/tree/master/Python-Solution/287_Find-the-Duplicate-Number)    


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
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        
        # 寻找在环内的相遇点
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        
        # 不存在环
        if slow != fast:
            return None
        
        # 找环入口
        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return fast
```