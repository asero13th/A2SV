class Solution:
    def racecar(self, target: int) -> int:
        q = deque([(0, 0, 1)]) 
        visited = set()

        while q:
            moves, position, velocity = q.popleft()

            if position == target:
                return moves
            
            if (position, velocity) in visited:
                continue
                
            visited.add((position, velocity))

            q.append((moves + 1, position + velocity, velocity * 2))

            if (position + velocity > target and velocity > 0) or (position + velocity < target and velocity < 0):
                velocity = -1 if velocity > 0 else 1
                q.append((moves + 1, position, velocity))
        
        
        return -1 
        