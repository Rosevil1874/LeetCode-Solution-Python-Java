# 84 - 柱状图中最大的矩形

## 栈
思路：  
1. 栈中存放一组高度值比当前元素高的柱子的下标；
2. 遍历数组：
    - 若当前柱子比栈顶（当前阶段最高的柱子）的高度低，说明当前元素无法和栈中保存的柱子们构成一个面积较大的矩形（强行加在一起的话当前柱子就成了木桶效应中的短板，面积反而会减小）。此时将栈中比当前柱子高的都弹出并计算面积，更新最大面积。
    - 否则说明此柱子并非短板，加上它可能增加当前正在构建的矩形的面积，直接将其下标压栈。
3. 计算最后一根柱子。
```java
class Solution {
    public int largestRectangleArea(int[] heights) {
        Stack<Integer> stack = new Stack<>();
        stack.push(-1);
        int maxArea = 0;
        int n = heights.length;

        for (int i = 0; i < n; i++) {
            while (stack.peek() != -1 && heights[i] < heights[stack.peek()]) {
                int h = heights[stack.pop()];
                int w = i - stack.peek() - 1;
                maxArea = Math.max(maxArea, w*h);
            }
            stack.push(i);
        }

        while(stack.peek() != -1) {
            maxArea = Math.max(maxArea, heights[stack.pop()] * (n - stack.peek() - 1));
        }
        return maxArea;
    }
}
```