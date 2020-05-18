# 23 - 合并K个元素的有序链表


>审题：  
合并俩有序链表的,[传送门：合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/description/)。当时最简洁的方法是使用了递归，现在是K个链表的话，一个个连铁定超时没得跑的。  
怎么办呢，偷偷瞟一眼相关话题，有**堆**和**分治算法**。哎，第一反应就是把算法书翻出来再学一遍，虽然前面已经几乎两遍了，算法助教说的果然没错，这本书是值得花时间的。


## 分治算法
1. 对半划分直到只有一个或两个链表；
2. 使用合并两个有序链表的方法合并。
以4链表为例：
	1、3合并，合并结果放到1的位置；
	2、4合并，合并结果放到2的位置；
	再把1、2合并（相当于原来的13 和 24合并）。
```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        // corner cases
        if (l1 == null) {
            return l2;
        } else if (l2 == null) {
            return l1;
        } else {
            if (l1.val <= l2.val) {
                l1.next = mergeTwoLists(l1.next, l2);
                return l1;
            } else {
                l2.next = mergeTwoLists(l1, l2.next);
                return l2;
            }
        }
    }

    public ListNode mergeKLists(ListNode[] lists) {
        int n = lists.length;
        if (n == 0) {
            return null;
        }

        while (n > 1) {
            int k = (n + 1) / 2;
            for (int i = 0; i < n / 2; i++) {
                lists[i] = mergeTwoLists(lists[i], lists[i + k]);
            }
            n = k;
        }
        return lists[0];
    }
}
```


## 最小堆
1. 把k个链表的首元素加入最小堆中，使其升序排列；
2. 每次取出堆顶元素（最小）加入结果链表，然后将其后那个元素加入最小堆；
3. 直到把堆取空了，结果链表就合并完成了。

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        // 建立最小堆
        Queue<ListNode> pq = new PriorityQueue<>((v1, v2) -> v1.val - v2.val);
        for (ListNode node: lists) {
            if (node != null) {
                pq.offer(node);
            }
        }

        // 新链表
        ListNode dummyHead = new ListNode(0);
        ListNode curr = dummyHead;
        while (!pq.isEmpty()) {
            ListNode minNode = pq.poll();
            curr.next = minNode;
            curr = curr.next;
            if (minNode.next != null) {
                pq.offer(minNode.next);
            }
        }
        return dummyHead.next;
    }
}

```