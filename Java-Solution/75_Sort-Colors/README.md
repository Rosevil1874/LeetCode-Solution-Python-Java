# 75 - 分类颜色

## 题目描述
![problem](images/75.png)

## 题解

**思路**
1. 不管白色（1），把红色(0)和蓝色(2)移到对应位置就行；
2. 两个指针，red指向最后一个归位的红色，blue指向第一个归位的蓝色；
3. 遍历数组，每遇到一个红色就插入到red后面并更新指针位置，每遇到一个蓝色就插入到blue前面并更新blue指针位置。

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        red, blue = 0, n - 1
        
        i = 0
        while i <= blue:
            if nums[i] == 0:
                nums[i], nums[red] = nums[red], nums[i]
                red += 1
            elif nums[i] == 2:
                nums[i], nums[blue] = nums[blue], nums[i]
                i -= 1      # 换到前面的数值是未经判断的，i-1会保持i的位置以检查此元素
                blue -= 1
            i += 1
        
```