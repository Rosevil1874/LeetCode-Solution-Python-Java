# 48 - 旋转图像

## 环形旋转
这道题可以说是非常经典了，会不会每新学一门语言就要再写一次啊_(°ω°｣∠)_  不过以前是直接将矩阵旋转90°输出，而不是改变原矩阵。那么就用交换吧，emmm但是看了一下，交换的话得同时交换四个方向的元素，好麻烦啊啊啊。

```java
class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        for (int i = 0; i < n/2; i++) {
            for (int j = i; j < n - i - 1; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[n - j - 1][i];
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1];
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1];
                matrix[j][n - i - 1] = temp;
            }
        }
    }
}
```


## 反转+对角线交换

一、顺时针旋转90°
1. 上下翻转；
2. 对角线对换。

```java
class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;

        // 对角线翻转
        for (int i = 0; i < n; i++) {
            for(int j = i; j < n; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        
        // 上下翻转
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n/2; j++){
                int temp = matrix[i][j];
                matrix[i][j] = matrix[i][n - j - 1];
                matrix[i][n - j - 1] = temp;
            }
        }

    }
}           
```


二、逆时针旋转90°
1. 左右翻转；
2. 对角线对换。
