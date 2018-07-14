# 667 - Beautiful Arrangement II 【优美的排列】

## 题目描述
![problem](images/667.png)


### 题解：  
第一反应是判断相邻两个数中非升序的情况的数量，若大于一则不可行。所以我的第一版代码是这样的：
```python
cnt = 0
for i in range( 1, len(nums) ):
    if nums[i] < nums[i - 1]:
        cnt += 1
        if cnt > 1:
            return False

return True
```

但是这版代码我并没有运行，因为我知道没有这么简单哈哈，题目上给的例子太少了，像这样  
`[4, 4, 2, 3, 3, 6]`  
就行不通了，需要修改两个4，但以上代码却只能检测到一个。  
所以我们需要在判断相邻数字大小关系后进一步判断应该如何修改以最小代价得到非递减数列。  
**综上**  
1. 首先比较的是i和i-1位置上的数字，若这两个数不是非递减关系，转第二步；
2. 若i数字大于等于i-2位置上的数字（满足非递减），那么就修改i-1位置上的数字(修改为和i位置相同)；
3. 否则修改i位置上的数字(修改为和i-1位置相同)。

**AC代码**  
```python
class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cnt = 0
        for i in range( 1, len(nums) ):
            if nums[i] < nums[i - 1]:
                cnt += 1
                if cnt > 1:
                    return False
                if i == 1 or nums[i] >= nums[i - 2]:
                    nums[i - 1] = nums[i]
                else: 
                    nums[i] = nums[i - 1]
        return True
```