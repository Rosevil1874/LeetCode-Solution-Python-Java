# 23 - 合并K个元素的有序链表

## 题目描述
![problem](images/23.png)

>审题：  
首先吧，这个题目我就没看懂，合并有序链表并返回有序链表，excuse me？？
然后吧，看了一下输入输出type，索德斯呢~~ k个链表都是有序的，合并成一个/摊手  
最后吧，想起来之前做过一个合并俩有序链表的,[传送门：合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/description/)。当时最简洁的方法是使用了递归，现在是K个链表的话，一个个连铁定超时没得跑的。  
怎么办呢，偷偷瞟一眼相关话题，有**堆**和**分治算法**。哎，第一反应就是把算法书翻出来再学一遍，虽然前面已经几乎两遍了，算法助教说的果然没错，这本书是值得花时间的。


## 分治算法
1. 对半划分直到只有一个或两个链表；
2. 使用合并两个有序链表的方法合并。
以4链表为例：
	1、3合并，合并结果放到1的位置；
	2、4合并，合并结果放到2的位置；
	再把1、2合并（相当于原来的13 和 24合并）。
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        l = len(lists)
        if l == 0:
            return None
        while l > 1:
            k = (l + 1) // 2
            for i in range(l // 2):
                lists[i] = mergeTwoLists(lists[i], lists[i + k])
            l = k
        return lists[0]

    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        elif not l2:
            return l1
        else:
            if l1.val < l2.val:
                l1.next = self.mergeTwoLists(l1.next, l2)
                return l1
            else:
                l2.next = self.mergeTwoLists(l1, l2.next)
                return l2
```
递归深度超限了orz,Python中默认的最大递归深度是989，当尝试递归第990时便出现递归深度超限的错误:
![error](images/error.png)

虽然可以手动设置递归调用深度：
```python
import sys
sys.setrecursionlimit(10000000)
```
但是我不要，我！不！要!/傲娇脸
应该是合并两个链表也是递归，所以就好多好多递归所以超了吧。
把合并两个数组改一下：
```python
def mergeTwoLists(self, l1, l2):
    head = ListNode(0)
    res = head
    while l1 and l2:
        if l1.val < l2.val:
            res.next = l1
            l1 = l1.next
        else:
            res.next = l2
            l2 = l2.next
        res = res.next
    if l1:
        res.next = l1
    elif l2:
        res.next = l2
    return head.next
```
果然通过了哗哈哈哈哈哈哈哈哈哈哈哈✧\*｡٩(ˊᗜˋ*)و✧*｡


## 最小堆
1. 把k个链表的首元素加入最小堆中，使其升序排列；
2. 每次取出堆顶元素（最小）加入结果链表，然后将其后那个元素加入最小堆；
3. 直到把堆取空了，结果链表就合并完成了。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from heapq import heappush, heappop, heapreplace, heapify

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = curr = ListNode(0)
        # i代表的是第i条链表，若不把i加进去，则建堆过程中当链表头结点相同时会接着比较链表下一个结点
        h = [(head.val, i, head) for i, head in enumerate(lists) if head]
        heapify(h)              # 建立最小堆
        while h:
            val, i, node = h[0]
            if not node.next:   # 遍历完了堆顶链表，将其pop
                heappop(h)
            else:               # 使用堆顶链表的下一个结点替代这个结点
                heapreplace(h, (node.next.val, i, node.next))   # 删除最小元素值，添加新的元素值
            curr.next = node
            curr = curr.next
        return dummy.next
```