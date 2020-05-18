# 19 - 删除链表的倒数第N个节点


## 双指针
1. 使用两个指针，一快一慢；
2. 快的比慢的快N个结点；
3. 当快的到达尾部的时候，慢的正好指向目标结点的pre结点，只需要轻轻跳过它就Okey-dokey yo!
4. 遍历一遍，妙哉妙哉(｡◕ˇ∀ˇ◕)

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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        // coner case 1
        if (head == null) {
            return head;
        }

        ListNode fast = head;
        ListNode slow = head;

        // 快指针先走n步
        for (int i = 0; i < n; i++) {
            fast = fast.next;
        }

        // coner case 2: 当n等于链表长度时fast会移动到最后的null节点，倒数第n个节点即第一个节点
        if (fast == null) {return head.next;}

        // 快慢指针一起向前，当快指针到结尾时慢指针刚好在待删节点的前面
        while (fast.next != null) {
            fast = fast.next;
            slow = slow.next;
        }
        // 删除节点
        slow.next = slow.next.next;
        return head;
    }
}

```