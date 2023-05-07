class Solution:
    
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
   

        x, y = entrance
        
        maze[x][y] = "*"
        max_row, max_col = len(maze) - 1, len(maze[0]) - 1

        queue = deque([(x, y, 0)])
        offsets = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while queue:
            r, c, steps = queue.popleft()

            
            if steps > 0 and (r == 0 or c == 0 or r == max_row or c == max_col):
                return steps

            
            for dr, dc in offsets:
                dr, dc = r + dr, c + dc

                
                if dr < 0 or dc < 0 or dr > max_row or dc > max_col or maze[dr][dc] != ".":
                    continue

                queue.append((dr, dc, steps + 1))
                maze[dr][dc] = "*"

        return -1
        
#         def bfs(entrance):
#             queue = deque([entrance])
#             x, y = entrance
#             visited = {(x, y)}
            
            
#             move = 0
#             while queue:
                
#                 direction = [[0,1],[1,0],[0,-1],[-1,0]]
#                 for i in range(len(queue)):
#                     node =  queue.popleft()
                    
#                     for x, y in direction:
#                         i, j = node
                        
#                         if 0 <= (x+i)<len(maze) and 0 <=(y+j)<len(maze[0]) and (x+i,y+j) not in visited and maze[x + i][y + j] == ".":
#                             queue.append([x + i, y + j])
#                             visited.add((x + i, y + j))
                            
#                             if (0 == x + i or len(maze) - 1 == x + i) or (0 == y + j or len(maze[0]) - 1 == y + j ):
#                                         return move + 1
                
#                 if queue:
#                     move += 1
#             return move
#         ans = bfs(entrance)
#         return ans if ans != 0 else -1
                                    
                                        
                    
                    
                
                
            
            
            
            
        