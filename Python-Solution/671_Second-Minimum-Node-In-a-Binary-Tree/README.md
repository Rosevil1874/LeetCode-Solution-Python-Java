# 671 - 二叉树中第二小的节点

## 题目描述
![problem](images/671.png)

>关联题目： [230. 二叉搜索树中第K小的元素](https://github.com/Rosevil1874/LeetCode/tree/master/Python-Solution/230_Kth-Smallest-Element-in-a-BST)


## 题解一：【DFS】
**思路：**
1. 根节点一定是最小的节点；
2. 遍历二叉树，每次找到大于根节点并小于当前节点的值a；
3. 遍历完之后a就是大于根节点（最小值）且小于其他所有节点的第二小节点啦。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        res = [float('inf')]
        self.dfs(root, root, res)
        return -1 if res[0] == float('inf') else res[0]
        
    def dfs(self, root: TreeNode, curr: TreeNode, res: List[int]) -> List[int]:
        if not curr:
            return
        if root.val < curr.val < res[0]:
            res[0] = curr.val
        self.dfs(root, curr.left, res)
        self.dfs(root, curr.right, res)

```


## 题解二：【BFS】
**思路：**使用set：元素唯一，自动排序；emmmmm不过虽然set会自动排序，但是转成list之后还是会乱所以需要再排序一下。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root: return -1
        
        queue = [root]
        vals = set()
        
        while queue:
            node = queue.pop(0)
            vals.add(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        if len(vals) == 1: return -1
        return sorted(list(vals))[1]
```