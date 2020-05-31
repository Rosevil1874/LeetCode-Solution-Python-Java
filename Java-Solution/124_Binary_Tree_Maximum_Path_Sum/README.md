# 124 - 二叉树中的最大路径和

## 题目描述
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.


## 递归
思路： 最长路径 = 最长左子路径 + 最长右子路径

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
    private int maxSum = Integer.MIN_VALUE;

    private int findMax(TreeNode node) {
        if (node == null) return 0;

        // 计算左右子树最长路径, 取最长路径(大于0时)或0
        int left = Math.max(findMax(node.left), 0);
        int right = Math.max(findMax(node.right), 0);

        // 更新maxSum
        maxSum = Math.max(maxSum, node.val + left + right);

        // 返回左右子路径中较长的一个，否则不能构成路径
        return node.val + Math.max(left, right);
    }

    public int maxPathSum(TreeNode root) {
        findMax(root);
        return maxSum;
    }
}
```