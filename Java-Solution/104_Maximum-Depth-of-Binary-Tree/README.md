# 104 - 二叉树的最大深度
## 题目描述
![problem](images/104.png)

>关联题目： [111. 二叉树的最小深度](https://github.com/Rosevil1874/LeetCode/tree/master/Python-Solution/111_Minimum-Depth-of-Binary-Tree)


## 题解一：recursive
**思路：** 递归求解：二叉树的最大深度 = max(左子树的最大深度, 右子树的最大深度) + 1；后面加上的这个1是根节点这一层。

>
1. 时间复杂度：最好的情况树是平衡的，树高为log(N),此时时间复杂度为O(logN)；最坏情况树完全不平衡，树高为N，此时时间复杂度为O(N);  
2. 空间复杂度：O(N).

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
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
    }
}
```


## 题解二：BFS

事实上说成层次遍历更准确一些啦~
>
1. 时间复杂度O(N);
2. 空间复杂度O(N)。

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
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        LinkedList<TreeNode> q = new LinkedList<>();
        q.add(root);
        int depth = 0;

        while (!q.isEmpty()) {
            depth += 1;
            int size = q.size();
            for (int i = 0; i < size; i++) {
                TreeNode node = q.poll();
                if (node.left != null) q.add(node.left);
                if (node.right != null) q.add(node.right);
            }
            
        }
        return depth;
    }
}
```