# 160 - 相交链表

## 题解
1. 将两链表相连成两个新链表：A+B和B+A；
2. 两个新链表的长度相同且有与两原始链表相同的交点，遍历两链表，若找到交点则返回，找不到则会同时遍历到链表尾部的null并返回。

```Java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if (headA == null || headB == null){
            return null;
        }

        ListNode p1 = headA, p2 = headB;
        while (p1 != p2) {
            p1 = p1 == null ? headB : p1.next;
            p2 = p2 == null ? headA : p2.next;
        }
        return p1;
    }
}           
```