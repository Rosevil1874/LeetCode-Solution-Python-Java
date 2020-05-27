# 83 - 删除排序链表中的重复元素

## 双指针
1. 指针1指向不重复的最后一个结点；
2. 指针2依次扫描，若不重复则更新指针1，否则移除。

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
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        ListNode tail = head;    // 不重复的最后一个节点
         ListNode p = head.next;
        while (p != null) {
            if (p.val == tail.val) {
                p = p.next;
                tail.next = tail.next.next;
            } else {
                p = p.next;
                tail = tail.next;
            }
        }
        return head;
    }
}
```