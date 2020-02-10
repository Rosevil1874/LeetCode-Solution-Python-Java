# 315 - [计算右侧小于当前元素的个数 ](https://leetcode.com/problems/count-of-smaller-numbers-after-self/)

## 题目描述
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

**Example:**

	Input: [5,2,6,1]
	Output: [2,1,1,0] 
	Explanation:
	To the right of 5 there are 2 smaller elements (2 and 1).
	To the right of 2 there is only 1 smaller element (1).
	To the right of 6 there is 1 smaller element (1).
	To the right of 1 there is 0 smaller element.


## 题解
merge sort：一个元素右边小于它的值，是在有序序列中本该在其左边的元素jump到了右边。  

```python
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def sort(indexes):
            half = len(indexes) // 2
            if half:
                # 分割直到indexes中只有一个元素再merge
                left, right = sort(indexes[:half]), sort(indexes[half:])
                for i in range(len(indexes))[::-1]:
                    # 此时left和right都已经有序
                    # 1. not right: 右半部分没有了，左半部分是有序的，可以直接将左边的pop
                    # 2. left最后一个值大于right最后一个值→left最后一个值大于right所有值
                    # 每次pop当前序列中的最大值到结果序列尾部，就完成了子序列的排序
                    if not right or (left and nums[left[-1]] > nums[right[-1]]):
                        smaller[left[-1]] += len(right)
                        indexes[i] = left.pop()
                    else:
                        indexes[i] = right.pop()
            return indexes
        
        smaller = [0] * len(nums)
        sort(list(range(len(nums))))
        return smaller
```