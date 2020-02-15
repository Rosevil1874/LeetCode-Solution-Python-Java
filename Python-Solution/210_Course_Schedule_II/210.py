class Solution:
    def findOrder(self, numCourses: int, prerequisites) :
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
        return res if len(queue) == numCourses else []
        
        

s = Solution()
r = s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
print(r)