class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def bfs(node):
            queue = deque([node])
            visited = set({0})
      
            while queue:
                node  = queue.popleft()

                
                for i in range(len(node)):
           
                    if node[i] not in visited:
                        visited.add(node[i])
                        queue.append(rooms[node[i]])
        
           
            return True if len(visited) == len(rooms) else False
        return bfs(rooms[0])
                        
        
            