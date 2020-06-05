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
```Java
public class Trie {
    private boolean is_string = false;
    private Trie next[] = new Trie[26];

    public Trie(){}

    //插入单词
    public void insert(String word){
        Trie root = this;
        char w[] = word.toCharArray();
        for(int i = 0; i < w.length; i++){
            // 不存在: 创建一个新的节点，并将它与父节点的相连
            if(root.next[w[i]-'a'] == null) root.next[w[i]-'a']=new Trie();
            // 存在: 移动到树的下一个子层,继续搜索下一个键字符。
            root = root.next[w[i]-'a'];
        }
        // 达到最后一个字符，标记匹配
        root.is_string = true;
    }

    //查找单词
    public boolean search(String word){
        Trie root = this;
        char w[] = word.toCharArray();
        for(int i = 0; i < w.length; i++){
            if(root.next[w[i]-'a'] == null) return false;
            root = root.next[w[i]-'a'];
        }
        return root.is_string;
    }
    
    //查找前缀
    public boolean startsWith(String prefix){
        Trie root = this;
        char p[] = prefix.toCharArray();
        for(int i = 0;i<p.length;++i){
            if(root.next[p[i]-'a'] == null)return false;
            root = root.next[p[i]-'a'];
        }
        // 和查找单词的唯一区别：前缀匹配就能返回true，不需要达到单词末尾
        return true;
    }
}
```