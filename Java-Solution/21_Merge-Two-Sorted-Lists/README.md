# 21 - 合并两个有序链表


## 老老实实翻开数据结构合并吧
1. 判断链表是否为空，若链表为空则返回空链表；
2. 创建一个新的空链表；
3. 创建一个指针pre指向新链表头；
4. 依次判断两个旧链表头结点val大小，pre指向小的那个，且将这个“小链表”的头指针删去；
5. 其中一个旧链表全部接到新链表后，将另一个链表剩下的部分接到新链表。
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
        if (l1 == null && l2 == null) {
            return null;
        } else if (l1 == null) {
            return l2;
        } else if (l2 == null) {
            return l1;
        }

        // 新链表头节点
        ListNode new_head = new ListNode(-1);
        ListNode curr = new_head;

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
        curr.next = l1 != null ? l1 : l2;

        return new_head.next;
    }
}
```


## 递归
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
}
```