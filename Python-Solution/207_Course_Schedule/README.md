# 207 - [课程表](https://leetcode.com/problems/course-schedule/)

## 题目描述
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?


**思考**：此题是一个经典的拓扑排序问题，可以使用DFS解决。


## 1. DFS (recursive)
对比下来并不喜欢这个方法，不够直观（也不太好记忆哈哈哈），觉得下一个DFS方法更直观便于理解。

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]
        
        # 记录在每一个课程后面完成的课程: create graph
        for a, b in prerequisites:
            graph[a].append(b)
          
        # dfs遍历每一条边，若当前边所在路径存在环则返回False
        for i in range(numCourses):
            if not self.dfs(graph, visit, i):
                return False
        return True
    
        
    def dfs(self, graph: List[List[int]], visit: List[int], i: int) -> bool:
        # i在当前路径正在访问中，则还有后继结点未访问的情况下存在环，返回False
        if visit[i] == -1:
            return False
        
        # i在当前路径已经访问过了，且其所有后继课程已经访问过，此路径可行
        if visit[i] == 1:
            return True
        
        # 添加正在访问标记
        visit[i] = -1
        
        # 访问所有的后继课程（邻居结点），若在任何一个结点处存在环则返回False
        for j in graph[i]:
            if not self.dfs(graph, visit, j):
                return False
        # 访问过所有后继结点后将i标记问访问过
        visit[i] = 1
        return True
```


## 2. DFS (stack)
```python
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        forward = {i: set() for i in range(numCourses)}
        backward = defaultdict(set)
        
        # 分别记录每个结点的所有后继/前驱结点
        for a, b in prerequisites:
            forward[a].add(b)
            backward[b].add(a)
            
        # stack中存放所有没有前置结点的课程
        stack = [node for node in range(numCourses) if not backward[node]]
        while stack:
            node = stack.pop()
            # 对其每一个后继结点，删除他们的前驱结点node，表示已经访问过
            for successor in forward[node]:
                backward[successor].remove(node)
                # 已经没有前驱结点的课程放入stack
                if not backward[successor]:
                    stack.append(successor)
            # 当前课程可以成功完成？？？这里还是不太懂？？？？？？？？
            backward.pop(node)
                    
        # 所有课程的前驱结点都访问完毕，可行
        return not backward
```

## 3. BFS
和BFS只是使用栈(stack)还是队列(queue)的区别。
```python
from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        forward = {i: set() for i in range(numCourses)}
        backward = defaultdict(set)
        
        # 分别记录每个结点的所有后继/前驱结点
        for a, b in prerequisites:
            forward[a].add(b)
            backward[b].add(a)
            
        # queue中存放所有没有前置结点的课程
        queue = deque(node for node in range(numCourses) if not backward[node])
        cnt = 0
        while queue:
            node = queue.popleft()
            cnt += 1
            # 对其每一个后继结点，删除他们的前驱结点node，表示已经访问过
            for successor in forward[node]:
                backward[successor].remove(node)
                # 已经没有前驱结点的课程放入stack
                if not backward[successor]:
                    queue.append(successor)
                    
        # 所有课程的前驱结点都访问完毕，可行
        return cnt == numCourses
```

简化版：
```python
from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        G = [[] for _ in range(numCourses)]   
        degree = [0] * numCourses
        
        # 分别记录每个结点的所有后继结点、入度
        for a, b in prerequisites:
            G[a].append(b)
            degree[b] += 1
            
        # queue中存放所有没有前置结点的课程
        queue = [node for node in range(numCourses) if degree[node] == 0]
        cnt = 0
        for node in queue:
            # 对其每一个后继结点，入度减一，表示已经访问过node
            for successor in G[node]:
                degree[successor] -= 1
                # 已经没有前驱结点的课程放入stack
                if degree[successor] == 0:
                    queue.append(successor)
                    
        # 所有课程的前驱结点都访问完毕，可行
        return len(queue) == numCourses
```