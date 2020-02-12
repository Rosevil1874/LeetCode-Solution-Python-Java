# 140 - 单词拆分II

## 题目描述
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

**Note:**

	The same word in the dictionary may be reused multiple times in the segmentation.
	You may assume the dictionary does not contain duplicate words.

**Example 1:**

	Input:
	s = "catsanddog"
	wordDict = ["cat", "cats", "and", "sand", "dog"]
	Output:
	[
	  "cats and dog",
	  "cat sand dog"
	]

**Example 2:**

	Input:
	s = "pineapplepenapple"
	wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
	Output:
	[
	  "pine apple pen apple",
	  "pineapple pen apple",
	  "pine applepen apple"
	]
	Explanation: Note that you are allowed to reuse a dictionary word.

**Example 3:**

	Input:
	s = "catsandog"
	wordDict = ["cats", "dog", "sand", "and", "cat"]
	Output:
	[]


## DFS

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self.helper(s, wordDict, {})
    
    # memo：存储一个子串内对应的单词序列
    def helper(self, s: str, wordDict: List[str], memo: dict) -> List[str]:
        if s in memo:
            return memo[s]
        if len(s) == 0:
            return []
        
        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if word == s:
                res.append(word)
            else:
                result_of_the_rest = self.helper(s[len(word):], wordDict, memo)
                for item in result_of_the_rest:
                    item = word + ' ' + item
                    res.append(item)
        memo[s] = res
        return res
            
```
