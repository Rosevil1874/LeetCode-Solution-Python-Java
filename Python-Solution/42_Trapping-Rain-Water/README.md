# 42 - 接雨水

## 题目描述
![problem](images/42.png)

>审题：  
1. 面积计算；
2. 短板效应。

## 题解

>思路：
1. 以逐个累计的方式替代长×宽的方式；
2. 从左往右记录一个最高点，若其右的值大于它，即为新的最高点，否则可以将其面积计入；
3. 从右往左记录一个最高点，若其左的值大于它，即为新的最高点，否则可以将其面积计入；
4. 左右指针相遇在最高点结束算法。

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        left, right = 0, len(height) - 1
        max_left, max_right = 0, 0
        
        while left <= right:
            if height[left] <= height[right]:
                if height[left] < max_left:
                    water += (max_left - height[left])
                else:
                    max_left = height[left]
                left += 1
            else:
                if height[right] < max_right:
                    water += (max_right - height[right])
                else:
                    max_right = height[right]
                right -= 1
        return water
```

## 简化代码
```python
class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        left, right = 0, len(height) - 1
        max_left, max_right = 0, 0
        
        while left <= right:
            max_left = max(max_left, height[left])
            max_right = max(max_right, height[right])
            
            if max_left < max_right:
                water += max_left - height[left]
                left += 1
            else:
                water += max_right - height[right]
                right -=1
        return water
            
        return water
```