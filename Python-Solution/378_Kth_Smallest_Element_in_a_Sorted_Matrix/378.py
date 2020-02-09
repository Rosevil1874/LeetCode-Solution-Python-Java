from heapq import *
class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        min_heap = []
        
        # 将第一行的元素放入最小堆中（堆中不需要超过k个元素）
        # 由于输出的是第k小的元素而不是第k小的不同的值，需要同时记录元素位置以区分值相同的元素
        # 元素值必须放在堆中节点元组的最前面，才能首先以其为标准排序
        for j in range(len(matrix[0])):
            heappush(min_heap, (matrix[0][j], 0, j))
        
        # 依次从堆顶弹出最小值，同时加入当前元素的下方元素（矩阵中剩余的最小值）到堆中
        k_count = 0 
        while min_heap:
            num, i, j  = heappop(min_heap)
            k_count += 1
            if k_count == k:
                break
            if i + 1 < len(matrix):
                heappush(min_heap, (matrix[i + 1][j], i + 1, j))
        return num
        	
        

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8
r = Solution().kthSmallest(matrix, k)
print(r)
