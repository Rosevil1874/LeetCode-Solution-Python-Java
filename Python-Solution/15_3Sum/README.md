# 15 - 三数之和

## 题目描述
![problem](images/15.png)

<!-- more -->

>审题：
这个这个，似曾相识呀，诶不就是第一题两数之和嘛
[两数之和-传送门](https://rosevil1874.github.io/2018/04/05/1.%E4%B8%A4%E6%95%B0%E4%B9%8B%E5%92%8C/#more)
So，可不可以把“三数之和”问题改成“两数之和+X”捏。。。

## 方法一：利用“两数之和”
1. 排序，方便去重
2. 字典中存放与出现过的数字能组成和为0的三元组的元素；
3. 遍历检查元素是否在字典中，在则构成三元组，否则将与当前两个元素能组成三元组的元素放入字典；
4. 使用set存放返回三元组去重，返回时转换回列表。

> Runtime: 712 ms, faster than 89.67% of Python3 online submissions

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = set()
        
        for i, val1 in enumerate(nums[:-2]):
            if i >= 1 and val1 == nums[i-1]:   # delete duplicate
                continue;
                
            d = {}  # save nums have chance in triplets
            for val2 in nums[i+1:]:
                if val2 not in d:
                    d[-val1 - val2] = 1
                else:
                    res.add((val1, val2, -val1-val2))
        return map(list, res)
```


## 方法二：双指针
1. 将数组排序；
2. 第一层循环遍历元素到倒数第三个【第一个数】；
3. 第二层循环使用双指针在剩余位置由两端向中间靠拢检查【后两个数】；
4. 符合条件且不重复的加入结果数组。

> Runtime: 908 ms, faster than 63.40% of Python3 online submissions

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        
        for i in range(n - 2):
            if i >= 1 and nums[i] == nums[i-1]:   # delete duplicate
                continue;
                
            j, k = i + 1, n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s < 0:
                    j += 1
                elif: s > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1; k -= 1
                    
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                
        return res
```
