# 114 - 二叉树展开为链表 

## 题目描述
Given a binary tree, flatten it to a linked list in-place.  
根据给的例子，是按先序遍历的顺序展开二叉树，去掉所有左子结点。


### 题解
> ref: [reversed preorder traverse](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/36977/)。从最右叶子节点开始依次将前一个结点的右指针指向自己，前一个结点的左指针指向空。可以看看评论中的图解，便于理解。

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode pre = null;

    public void flatten(TreeNode root) {
        if (root == null) return;

        flatten(root.right);
        flatten(root.left);
        root.right = pre;
        root.left = null;

        pre = root;
    }
}        
```
