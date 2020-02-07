# 44 - 通配符匹配

## 题目描述
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '\*'.
	'?' Matches any single character.
	'\*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

**Note:**
	s could be empty and contains only lowercase letters a-z.
	p could be empty and contains only lowercase letters a-z, and characters like ? or \*.
**Example 1:**
	Input:
	s = "aa"
	p = "a"
	Output: false
	Explanation: "a" does not match the entire string "aa".
**Example 2:**
	Input:
	s = "aa"
	p = "*"
	Output: true
	Explanation: '*' matches any sequence.
**Example 3:**
	Input:
	s = "cb"
	p = "?a"
	Output: false
	Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
**Example 4:**
	Input:
	s = "adceb"
	p = "*a*b"
	Output: true
	Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
**Example 5:**
	Input:
	s = "acdcb"
	p = "a\*c?b"
	Output: false


## 题解一
依次匹配。
```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = j = 0
        m, n = len(s), len(p)
        last_match = -1     # 使用*匹配序列时，上一个匹配的字符位置
        star_j = -1         # 上一个出现的*所在索引
        
        while i < m:
        	# 匹配一个字符，两指针向后
            if j < n and (p[j] == '?' or s[i] == p[j]):
                i += 1
                j += 1
            # pattern中出现*，pattern指针向后移一位
            elif j < n and p[j] == '*':
                last_match = i 
                star_j = j
                j += 1
            # 有一段子序列正在被*匹配，移动待匹配序列的指针
            elif last_match != -1:  
                j = star_j + 1
                last_match += 1
                i = last_match
            else:
                return False

        # 若字符串遍历完之后pattern还未匹配完，继续检查剩余部分
        while j < n and p[j] == '*':
            j += 1
        return j == n
                
                
```


## 题解二：有限状态机
Finite-state machine:
- 初始状态编号为0；
- 若遇到*，留在当前状态，因为*能匹配任意sequence（包括空字符串）；  
- 若遇到？或其他字符，进入一个新的状态，因为？只能匹配一个字符。

1. 首先通过遍历p构建一个有限状态机，其中的最后一个state是接受状态；
2. 再遍历s并运行有限状态机，检查遍历到每一个字符时可能处于的状态（一个集合）；
3. 如果某个状态与接受状态相同，则表示s与p是匹配的。

```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        transfer = {}
        state = 0
        
        # 构造有限状态机
        for c in p:
            if c == '*':
                # 处于状态state时遇到c → 进入下一个状态
                transfer[state, c] = state
            else:
                transfer[state, c] = state + 1
                state += 1
            
        acceptable = state
        state = set([0])
        # 遍历s检查是否有符合接受状态的state
        for c in s:
            state = set([transfer.get((at, token)) for at in state for token in [c,'*','?']])
        
        return acceptable in state
```