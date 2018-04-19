# 109 - 有序链表转换二叉搜索树

## 题目描述
![problem](images/109.png)

>审题：
1. 元素已经按升序排序好了；
2. BST：左子树任一结点小于当前结点，右子树任一结点大于当前结点；
3. AVL树：左右子树高度相差最多一层的BST树（通过旋转不平衡结点保持平衡）；
4. 中序遍历： 先访问左子结点（包括整棵子树），访问该节点，最后访问右子结点（包括整棵子树）。

## 递归 + 双指针
递归：
1. 由于BST树中序遍历得到的序列即为升序序列，因此可以将有序链表看作是BST中序遍历的结果；
2. 根据中序序列重构BST树，先找到根结点（中位数）；
3. 递归得寻找左右子树的根结点，即左右子序列的中位数；
4. 直到遍历完链表。

双指针：
1. 快慢指针，快指针步长为慢指针两倍；
2. 当快指针走到链表末尾时，慢指针在链表中点。

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        Rtree = self.findRoot(head)
        root = TreeNode(Rtree.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(Rtree.next)
        return root

    # 找到链表中点作为右子链表的起点返回，并将链表head后半部分切断
    def findRoot(self, head):
        if not head or not head.next:
            return head
        slow = head
        fast = head
        prev = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        return slow
```