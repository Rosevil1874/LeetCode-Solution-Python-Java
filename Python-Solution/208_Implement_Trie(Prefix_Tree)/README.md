# 208 - [实现Trie(前缀树)](https://leetcode.com/problems/implement-trie-prefix-tree/)

## 题目描述
Implement a trie with insert, search, and startsWith methods.

**Example:**
	Trie trie = new Trie();

	trie.insert("apple");
	trie.search("apple");   // returns true
	trie.search("app");     // returns false
	trie.startsWith("app"); // returns true
	trie.insert("app");   
	trie.search("app");     // returns true

**Note:**
1. You may assume that all inputs are consist of lowercase letters a-z.
2. All inputs are guaranteed to be non-empty strings.


## Trie树
前缀树(Trie树)又称字典树,是一种多叉树结构：
- 从根到某一个节点,拼接长字符串;
- 一个节点的子节点字符一定不相同；
- Trie提高效率,用空间换时间。


## 题解
```python
class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}
        
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    # 插入单词后将单词结束位置的is_word标记为真
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode()
            current = current.children[letter]
        current.is_word = True
        
        
    # 若整个单词遍历完的位置is_word标记为真，说明是一个完整单词
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current = self.root
        for letter in word:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return current.is_word
        
    
    # start_with不需要检查完整的单词，只要是单词的前面某一部分就可以
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current = self.root
        for letter in prefix:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```

使用defaultdict代替dict：
```python
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = defaultdict(TrieNode)
        
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    # 插入单词后将单词结束位置的is_word标记为真
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.is_word = True
        
        
    # 若整个单词遍历完的位置is_word标记为真，说明是一个完整单词
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current = self.root
        for letter in word:
            current = current.children.get(letter)
            if not current:
                return False
        return current.is_word
        
    
    # start_with不需要检查完整的单词，只要是单词的前面某一部分就可以
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current = self.root
        for letter in prefix:
            current = current.children.get(letter)
            if not current:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```