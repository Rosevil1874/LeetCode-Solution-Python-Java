# 142 - 环形链表 II

## 双指针
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


```Java
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        if (head == null || head.next == null) {
            return null;
        }

        // 判断是否有环，若有环，两指针相遇在环内
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                break;
            }
        }
        
        // 无环
        if (slow != fast) {
            return null;
        }

        // 寻找环入口
        slow = head;
        while (slow != fast) {
            slow = slow.next;
            fast = fast.next;
        }
        return slow;
    }
}
```