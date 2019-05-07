# 969 - 煎饼排序

## 题目描述
![problem](images/969.png)


## 题解一
**思路：**  
1. 找到最大值；
2. 把最大值反转到head；
3. 把最大值反转到tail；
4. 减少反转的size（就是不用管尾巴上的最大值啦）；
repeat...

>每把一个当前最大值移动到最后需要两次反转，最多2\*len(A)次反转，符合题意哒~

```python
class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = []
        sorted_A = sorted(A)
        size = len(A)

        while size > 1:
        	index = A.index( max(A) )			# 最大值索引
        	res.extend([index + 1, size])		# 将最大值反转到最后的两次操作
        	A = A[:index][::-1] + A[index+1:]	# 第一次反转以及删掉了最大值
        	A.reverse()							# 第二次反转
        	size -= 1

        return res
```

more concise solution：
```python 
class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = []
        for x in sorted(A)[::-1]:
        	index = A.index(x)
        	res.extend([index+1, x])
        	A = A[:index:-1] + A[:index]
        return res
```