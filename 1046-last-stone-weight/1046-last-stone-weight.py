class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
    
  
        
        while len(heap) > 1:
         
            x = -1 * heapq.heappop(heap)
            y = -1 * heapq.heappop(heap)
            
  
            
            if y != x:
                val = x - y
                heapq.heappush(heap,  -1 * val)
                
        return -1 * heap[0] if heap else 0
                
        