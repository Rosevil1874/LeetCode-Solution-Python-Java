# 85 - 最大矩形
## 题目描述
![problem](images/85.png)

>关联题目： [84.  柱状图中最大的矩形](https://github.com/Rosevil1874/LeetCode/tree/master/Python-Solution/84_Largest-Rectagel-in-Histogram)

## 题解
第一反应是DFS，不过这道题要是不要求形状必须为矩形的话，DFS还是可行的，但是。。。  
so，结合到此题是84题的拓展，可以思考如何把两道题联系起来，叮！把这个二维矩阵看成是抽象的柱子不就行了，分别以每一行作为底边，对每一列计算柱子的高为最长连续“1”的个数，就转化成了84题中的一个柱状图(｡◕ˇ∀ˇ◕)

```python
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not len(matrix) or not len(matrix[0]):
            return 0
        
        cols = len(matrix[0])
        height = [0]*(cols+1)    # 保存每一列中含连续1的个数（柱子的高度）,多加一个元素作为哨兵以正确计算最后一个柱子
        max_area = 0
        
        for row in matrix:
            # 计算到此行为止每一列重‘1’的个数
            for i in range(cols):
                height[i] = height[i] + 1 if row[i] == '1' else 0
                
            stack = [-1]        # 栈中存放一组高度值比当前元素高的柱子的下标
            for i in range(len(height)):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1]
                    max_area = max(max_area, w*h)
                stack.append(i)
        return max_area
```
