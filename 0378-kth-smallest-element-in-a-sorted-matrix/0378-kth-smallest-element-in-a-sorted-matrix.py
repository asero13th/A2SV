class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for i, row in enumerate(matrix):
            for j, val in enumerate(matrix[i]):
                heapq.heappush(heap, -val)
                
                if len(heap) > k:
                    heapq.heappop(heap)
                    
        return -heap[0]
                
        
        