class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        heap = []
        for pile in piles:
            heapq.heappush(heap, -1 * pile)
            
            
        for i in range(k):
            value =   heapq.heappop(heap)
            val = floor(value/2)
            heapq.heappush(heap,  val)
        print(heap)
        return -1 * sum(heap)
        