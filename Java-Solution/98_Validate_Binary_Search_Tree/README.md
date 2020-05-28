# 98 - 验证二叉搜索树

## 题目描述
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


## 递归
```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean isValidBST(TreeNode root) {
        return helper(root, null, null);
    }

    private boolean helper(TreeNode node, Integer lower, Integer upper) {
        if (node == null) {
            return true;
        }

        int val = node.val;

        if (lower != null && val <= lower) return false;
        if (upper != null && val >= upper) return false;

        if ( !(helper(node.left, lower, val)) ) return false;
        if ( !(helper(node.right, val, upper)) ) return false;

        return true;
    }
}
```

## 栈
二叉搜索树的中序遍历是升序序列，因此可以用栈的方法进行中序遍历，在遍历的同时比较前后遍历节点的大小。类似的解法有94题。

```Java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean isValidBST(TreeNode root) {
        if (root == null) {
            return true;
        }

        TreeNode pre = null;
        TreeNode curr = root;
        Stack<TreeNode> stack = new Stack<>();

        while (curr != null || !stack.isEmpty()) {
            while (curr != null) {
                stack.push(curr);
                curr = curr.left;
            }
            curr = stack.pop();
            if (pre != null && pre.val >= curr.val) {
                return false;
            }
            pre = curr;
            curr = curr.right;
        }
        return true;
    }
} 
```
