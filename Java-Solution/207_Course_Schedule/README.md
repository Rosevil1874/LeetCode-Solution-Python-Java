# 207 - [课程表](https://leetcode.com/problems/course-schedule/)

## 题目描述
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?


**思考**：此题是一个经典的拓扑排序问题，可以使用DFS解决。


## DFS (stack)
```java
class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[] inDegrees = new int[numCourses];
        Queue<Integer> queue = new LinkedList<>();

        List<List<Integer>> adjacency = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) {
            adjacency.add(new ArrayList<>());
        }

        // 统计每门课程的入度和其出边
        for (int[] p: prerequisites) {
            inDegrees[p[0]]++;
            adjacency.get(p[1]).add(p[0]);
        }

        // 把所有入度为0的点放入队列
        for(int i = 0; i < numCourses; i++) {
            if (inDegrees[i] == 0) queue.add(i);
        }

        // DFS
        while (!queue.isEmpty()) {
            int pre = queue.poll();
            numCourses--;
            for (int curr: adjacency.get(pre)) {
                if (--inDegrees[curr] == 0) queue.add(curr);
            }
        }
        return numCourses == 0;
    }
}
```
