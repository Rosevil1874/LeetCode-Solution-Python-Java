# 94 - 二叉树的中序遍历

## 题目描述
Given a binary tree, return the inorder traversal of its nodes' values.  
Follow up: Recursive solution is trivial, could you do it iteratively?


## 一、递归
中序遍历：左-根-右。  
虽然题目说递归没啥意思还是写写吧。

> Runtime: 28 ms, faster than 63.29% of Python3 online submissions.

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
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        helper(root, res);
        return res;
    }

    private void helper(TreeNode root, List<Integer> res) {
        if (root != null) {
            helper(root.left, res);
            res.add(root.val);
            helper(root.right, res);
        }
    }
}    
```


## 二、迭代
使用栈实现：
1. 先从根结点开始一直向左遍历，到达最左叶子结点，同时将这些结点依次压栈；
2. 从栈中依次pop左子结点，将其值放入结果数组中，同时将当前结点的右子结点作为根重复操作1；
3. 重复上述两步直到栈空。

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
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        TreeNode curr = root;
        
        while (curr != null || !stack.isEmpty()) {
            while (curr != null) {
                stack.push(curr);
                curr = curr.left;
            }
            curr = stack.pop();
            res.add(curr.val);
            curr = curr.right;
        }

        return res;
    }
}    
```
