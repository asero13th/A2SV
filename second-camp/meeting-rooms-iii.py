class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
     
  
        hashmap = [0] * n
        busy = []
        available = [i for i in range(n)]
        
        meetings.sort()
            
        for start, end in meetings:
            
            while busy and busy[0][0] <= start:
               
                _ , room = heapq.heappop(busy)
                heapq.heappush(available, room)
            
            if available:
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))
            else:
                time, room = heapq.heappop(busy)
                heapq.heappush(busy, (time + end - start, room))
            
            hashmap[room] += 1
                
            
        return hashmap.index(max(hashmap))
                
        