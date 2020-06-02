# 148 - 链表排序

## 题目描述
![problem](images/148.png)

>审题
题目要求时间复杂度为O(nlogn) 且空间复杂度为常数级。
首先排除掉时间复杂度为O(n^2)的比较排序：冒泡、选择、插入，以及O(n^1.3)的希尔排序；
其次从剩下的快速排序、堆排序、归并排序中排除空间复杂度为O(nlogn)的快速排序和O(n)的归并排序。
So..虽然符合题意的是堆排序，但是要自己实现堆好麻烦。考虑到单链表的操作还是选归并吧。


## 方法一
1. 双指针：找到中间结点，将链表分成两个部分；
2. 递归：对前后每一部分分别归并排序；
3. 合并：将排好序的子链表合并。

```Java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        // 分割链表
        ListNode prev = head, slow = head, fast = head;
        while (fast != null && fast.next != null) {
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        prev.next = null;
        return mergeList(sortList(head), sortList(slow));
    }

    private ListNode mergeList(ListNode l1, ListNode l2) {
        if (l1 == null) {
            return l2;
        } else if (l2 == null) {
            return l1;
        } else if (l1.val <= l2.val) {
            l1.next = mergeList(l1.next, l2);
            return l1;
        } else {
            l2.next = mergeList(l1, l2.next);
            return l2;
        }
    }
}              
```


## 方法二
把merge改为迭代吧。
哈哈哈过了真开心呦呦✧*｡٩(ˊᗜˋ*)و✧｡

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
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        // 分割链表
        ListNode prev = head, slow = head, fast = head;
        while (fast != null && fast.next != null) {
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        prev.next = null;
        return mergeList(sortList(head), sortList(slow));
    }

    private ListNode mergeList(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;
        while (l1 != null && l2 != null) {
            if (l1.val <= l2.val) {
                curr.next = l1;
                l1 = l1.next;
            } else {
                curr.next = l2;
                l2 = l2.next;
            }
            curr = curr.next;
        }
        if (l1 != null) {
            curr.next = l1;
        } else {
            curr.next = l2;
        }
        return dummy.next;
    }
}            
```