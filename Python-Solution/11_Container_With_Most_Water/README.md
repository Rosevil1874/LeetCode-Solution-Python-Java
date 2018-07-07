# 11 - 盛最多水的容器

## 题目描述
![problem](images/11.png)

<!-- more -->

>审题：这个题目从字面意思上理解还是不太直观的，在纸上画画图就一目了然了。懒得慢慢画个好看的图，去人家的文章里找找，找到啦，还是个动图啊厉害厉害，不过这个图直接泄露了解题方法啊~~

![maxArea](images/maxArea.png)

## 方法
思路【这个和CCF有一题‘最大的矩形’异曲同工啊】：
1. 要装最多水，就要矩形面积最大；
2. 以短边作为计算高度，木桶效应嘛( ･´ω\`･ )；
3. 从最大宽度开始，即双指针从两端向中间遍历；
4. 每次更新最大面积，指针相遇时返回结果。

```python
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = len(height)
        maxArea = 0
        area = 0
        i = 0
        j = l - 1

        while i < j:
            if height[i] < height[j]:
                h = height[i]
                area = (j - i) * h
                i += 1
            else:
                h = height[j]
                area = (j - i) * h
                j -= 1
            maxArea = max(maxArea, area)

        return maxArea
```

## 新技能get
没有思路的时候，可以悄悄点开这个相关话题，下面列出来的点一般就是解题方法啊哈哈哈，我可真聪明(〃ﾉωﾉ)

![idea](images/idea.png)