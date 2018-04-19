# 1 - 两数之和 Two Sum

## 题目描述
![problem](images/1.png)

<!-- more -->

### 1. 粗暴，【超时】：
```python
class Solution:
    def twoSum(self, nums, target):
    	for i, a in enumerate(nums):
    		for j, b in enumerate(nums):
    			if i!=j and a+b == target:
    				return (i,j)
```

### 2. 先过滤掉明显不可能的元素，再粗暴，下标会变啊喂！【错误】
```python
class Solution:
    def twoSum(self, nums, target):
    	nums = list( filter(lambda x: x <= target, nums) )
    	for i, a in enumerate(nums):
    		for j, b in enumerate(nums):
    			if i!=j and a+b == target:
    				return (i,j)
```

### 3.使用字典，hash查找速度666【通过】
```python
class Solution:
    def twoSum(self, nums, target):
    	tmp = {}
    	for i, a in enumerate(nums):
    	    if target-a in tmp:
    	        return (tmp[target-a], i)
    	    else:
    	        tmp[a] = i
```