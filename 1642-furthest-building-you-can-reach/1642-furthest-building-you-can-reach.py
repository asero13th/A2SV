class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = [] #
        
        for idx, height in enumerate(heights):
          
           
            diff = heights[idx + 1] - height if idx < len(heights) - 1 else -1
            if len(heap) >= ladders  and diff > 0:
                
                minimum = heapq.heappop(heap) if heap else diff

                heapq.heappush(heap, max(diff, minimum))
                
                
                
                if bricks < min(diff, minimum):
                    return idx  
                
                bricks -= min(diff, minimum)
            elif diff > 0:
                heapq.heappush(heap, diff)

        return len(heights) - 1
                
                
                    
                    
                
        