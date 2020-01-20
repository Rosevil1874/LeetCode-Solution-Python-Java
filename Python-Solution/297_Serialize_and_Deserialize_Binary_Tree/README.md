# 297 - 二叉树的序列化与反序列化

## 题目描述
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.


### 题解
序列化：
1. 这里使用'#'表示空节点，以','表示一个结点值的结束（即','是节点间的分隔符）；
2. 使用先序遍历的顺序进行序列化：root→left→right。

反序列化：
1. 判断是否为空树：空字符串，或只有一个表示None的'#'；
2. 根据结点分隔符','将所有结点值提取到数组中；
3. 从前往后遍历结点：
	* 若结点值是数字：从下一个节点开始递归反序列化其左右子树，并拼接返回；
	* 若结点值是'#'，说明当前位置为None，直接返回None。


```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        def serialize_core(node):
            if node:
                vals.append(str(node.val))
                serialize_core(node.left)
                serialize_core(node.right)
            else:
                vals.append('#')
                
        vals = []
        serialize_core(root)
        return (',').join(vals)
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        def deserialize_core():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = deserialize_core()
            node.right = deserialize_core()
            return node
            
        vals = iter(data.split(','))
        return deserialize_core()
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
```
