# 85 - 最大矩形

## 题解
第一反应是DFS，不过这道题要是不要求形状必须为矩形的话，DFS还是可行的，但是。。。  
so，结合到此题是84题的拓展，可以思考如何把两道题联系起来，叮！把这个二维矩阵看成是抽象的柱子不就行了，分别以每一行作为底边，对每一列计算柱子的高为最长连续“1”的个数，就转化成了84题中的一个柱状图(｡◕ˇ∀ˇ◕)

```java
class Solution {
    public int maximalRectangle(char[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return 0;
        }

        // 保存每一列中含连续1的个数（柱子的高度）,多加一个元素作为哨兵以正确计算最后一个柱子
        int cols = matrix[0].length;
        int[] heights = new int[cols + 1];
        Arrays.fill(heights, 0);
        int maxArea = 0;

        for (char[] row: matrix) {
            // 计算每一列到此行为止的连续‘1’的个数
            for (int i = 0; i < cols; i++) {
                heights[i] = (row[i] == '1') ? heights[i] + 1 : 0;
            }

            Stack<Integer> stack = new Stack<>();
            stack.push(-1);

            for (int i = 0; i < heights.length; i++) {
                while (stack.peek() != -1 && heights[i] < heights[stack.peek()]) {
                    int h = heights[stack.pop()];
                    int w = i - stack.peek() - 1;
                    maxArea = Math.max(maxArea, h*w);
                }
                stack.push(i);
            }
        }

        return maxArea;

    }
}
```
