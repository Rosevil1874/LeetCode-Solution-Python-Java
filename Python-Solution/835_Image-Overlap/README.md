# 835 - 图像重叠

## 题目描述
![problem](images/835.png)


## 方法
1. 找出A矩阵中为1的坐标；
2. 找出B矩阵中为1的坐标；
3. 字典d:
	- key：矩阵A的移动方式(e.g. (1, 2)表示向右平移1个位置，向下平移2个位置 )
	- val：以这种方式平移时，重叠像素点的个数。
4. 找出d中最大的val即为结果。

```python
import collections
class Solution:
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        ans = 0
        d = collections.defaultdict(int)
        a = []
        b = []
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    a.append((i, j))
                if B[i][j] == 1:
                    b.append((i, j))

        for aa in a:
            for bb in b:
                dd = (bb[0] - aa[0], bb[1] - aa[1])
                d[dd] += 1
                ans = max(ans, d[dd])
        return ans
```
