class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        for pile in piles:
            heapq.heappush(heap, -pile)
        
        for _ in range(k):
            val = heapq.heappop(heap)
            val = (val//2)
            
            heapq.heappush(heap, val)
        
        return -sum(heap)
            
        