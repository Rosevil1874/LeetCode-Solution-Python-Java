# 17 - 电话号码的字母组合

## 题目描述
![problem](images/17.png)

<!-- more -->

## 方法

第一反应是全排列，但是怎么实现没有想到，久了没有刷过oj已经脑子生锈了。
从别人那里借鉴的【深搜 + 递归】
```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        
        begin = 0   #当前需要处理的digits的位置
        path = ''   #深搜路径
        res = []    #返回结果
        phone = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        self.deepSearch(digits, begin, path, res, phone)
        return res
    
    def deepSearch(self, digits, begin, path, res, phone):
        # 深搜触底，找到一个结果
        if len(path) == len(digits) :
            res.append(path)
            return

        # 遍历当前数字代表的所有字母
        for char in phone[digits[begin]]:
            # 从下一位开始到最后一位的组合情况
            self.deepSearch(digits, begin + 1, path + char, res, phone)

```

简化版：
```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        cmb = [''] if digits else []        
        phone = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        
        for digit in digits:
            cmb = [prev + curr for prev in cmb for curr in phone[digit]]
        return cmb
        
```