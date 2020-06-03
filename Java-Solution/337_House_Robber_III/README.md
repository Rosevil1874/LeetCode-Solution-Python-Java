# 337 - 打家劫舍Ⅲ

## 题目描述
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.


### 题解

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
    private int[] helper(TreeNode node) {
        if (node == null) {
            return new int[2];
        }

        int[] result = new int[2];

        // left[0],left[1]：小偷偷左子房间和左子房间下一间房间得到的最大收入
        int[] left = helper(node.left);
        int[] right = helper(node.right);
        // 偷当前节点
        result[0] = node.val + left[1] + right[1];
        // 不偷当前节点
        result[1] = Math.max(left[0], left[1]) + Math.max(right[0], right[1]);

        return result;
    }

    public int rob(TreeNode root) {
        int[] result = helper(root);
        return Math.max(result[0], result[1]);
    }
}
```
