# 206 - 反转链表

## 题目描述
Reverse a singly linked list.

**Example:**
	Input: 1->2->3->4->5->NULL
	Output: 5->4->3->2->1->NULL
**Follow up:**
A linked list can be reversed either iteratively or recursively. Could you implement both?

>审题：
1. 原地反转一个单链表；
2. 使用迭代和递归两种方法。


## 迭代
头插法：向后遍历，依次将结点插到第一个结点前。


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
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        ListNode curr = head;
        while (curr.next != null) {
            ListNode temp = new ListNode(curr.next.val);
            temp.next = head;
            head = temp;
            curr.next = curr.next.next;
        }
        return head;
    }
}
```


## 递归
>cr:[全面分析再动手的习惯：链表的反转问题（递归和非递归方式）](http://www.cnblogs.com/kubixuesheng/p/4394509.html)
思路：
1. 递归先走到链表末端；
2. 更新每个结点的next值，即将指针反向；
3. 每个指针反向就链表反转了。

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
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        // 递归：从前向后走到链表末端
        ListNode newHead = reverseList(head.next);
        // 递归收回阶段：从后往前依次(head从倒数第二个节点开始往前遍历)
        // 指针反向：将前置结点设为后结点的后置结点
        head.next.next = head;
        head.next = null;
        return newHead;
    }
}

```