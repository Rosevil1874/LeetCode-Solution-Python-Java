# 210 - [课程表 II](https://leetcode.com/problems/course-schedule-ii/)

>关联题目：  
- [207. 课程表](https://github.com/Rosevil1874/LeetCode/tree/master/Python-Solution/207_Course_Schedule)


## 题解
与207的区别在于此题需要输出上课的顺序。

```python
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        G = [[] for _ in range(numCourses)]
        degree = [0] * numCourses
        
        for a, b in prerequisites:
            G[a].append(b)      # 保存每门课程的所有后继课程
            degree[b] += 1      # 保存每门课程的入度
            
        # 保存所有入读为0的课程：可以直接修读
        queue = [course for course in range(numCourses) if degree[course] == 0]
        res = []
        for course in queue:
            # 访问course，其后继节点的入度减一
            res.append(course)
            for node in G[course]:
                degree[node] -= 1
                # 没有前驱课程则放入queue
                if degree[node] == 0:
                    queue.append(node)
        return res[::-1] if len(queue) == numCourses else []
        
```