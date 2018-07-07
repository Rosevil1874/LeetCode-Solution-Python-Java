# 442 - 数组中重复的数据

## 题目描述
![problem](images/442.png)

## 要求
1. 不用到任何额外空间  
2. 时间复杂度O(n)

### 题解一【失败】：
其实这个题目不算难，只是它的额外要求比较难。两个要求中任意满足一个的方法都可以很快得出，但是要同时满足两个的话，，我就有点捉急了。  
然而机智的我发现它的关联题目[448 找到所有数组中消失的数字](https://github.com/Rosevil1874/LeetCode/tree/master/Python-Solution/448_Find-All-Numbers-Disappeared-in-an-Array)中有我要的方法哈哈哈。哎主要问题还是太久没有刷题了，这方法本来应该记得的⊙︿⊙

**方法**  
1. 遍历数组，将每个数减一作为索引，将该位置的数改为负数；
2. 再次遍历数组，若某位置上的数还是正数，说明原数组中没有（此索引+1）这个数。

```python
class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []

        for x in nums:
        	nums[x - 1] = - nums[x - 1]

        for i in range(len(nums)):
        	if nums[i] >= 0:
        		res.append(i + 1)

        return res
```

然而，我忽视了数组里面有出现两次的和出现一次的，也有在1-n这个范围内一次也没有出现过的，而这个方法就会输出出现两次和一次都没出现过的数，SO...



## 题解二【AC】
SO什么，SO看了大神的思路呀，应该同是咱华夏子孙的YuxinCao同学。同样化为负数的思路，有一点点差别，而且人家只用了一次循环。  
**方法**  
1. 遍历数组，将每个数减一作为索引；
2. 若该索引处已经是负数，说明【索引+1】这个数已经出现过一次，将其加入返回数组；
3. 否则将该索引处的数化为负数。
```python
class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []

        for x in nums:
        	idx = abs(x) - 1
        	if nums[idx] < 0:
        		res.append(idx + 1)
        	nums[idx] = - nums[idx]

        return res
```